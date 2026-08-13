---
layout: post
category: misadventures
title: Open Relay Controller for the Motorola PMUN1046A
---

![Open Relay Controller Rev A PCB (green) installed in the PMUN1046A enclosure alongside the OEM Motorola relay board](/images/ORC/ORC_and_relays_in_PMUN1046A.jpg){: style="width: 60%; display: block; margin: 0 auto;"}

The Motorola PMUN1046A is a well-engineered Power Distribution Module, featuring 10 channels of 15 A fused switching. Fortunately, they are commonly available on the used market. Unfortunately, they can only communicate with proprietary Motorola equipment. I decided to make a replacement for the unit's internal controller PCB assembly which can speak CANopen or USB.

<!--more-->

The original Motorola control PCB, PN PMLN5640, actually speaks USB! The sealed RJ45 on the enclosure is a GCAI port broken out onto 8P8C: VBUS on pin 1, ground on pin 2, D+ on pin 7, D- on pin 8. GCAI is Motorola's Global Core Accessory Interface, the accessory connector on APX and XTL radios. Worth stating plainly, because the [RadioReference thread on this exact part](https://forums.radioreference.com/threads/motorola-pmun1046a-universal-relay-controller-for-09-control-head.497868/) guesses SB9600 and that guess is tempting - SB9600 is a well documented 5-byte-command serial bus with open-source tooling already written for it. Motorola's own documentation is unambiguous, though: the install manual labels this run the "GCAI to RJ45 Cable," and the service manual says the URC connects to the radio through the GCAI port. It's GCAI, so none of the SB9600 tooling applies. GCAI runs the same two conductors as either CMOS RS-232 or USB, and the radio picks which one by doing a 1-Wire read of the DS2433 accessory-ID EEPROM on the controller board first - so the board is a USB device, but only after a handshake that a radio does and I can't. Scope confirmed full-speed USB (83 ns bit time) with the host polling, but the board never answered a descriptor request. This wasn't worth attempting to debug, and I didn't feel like loading my own firmware onto the stock board either.

![ORC Rev A (green, right) and OEM PMUN1046A control PCB (blue, left), flat top-down view showing component layout on both boards](/images/ORC/side_by_side_top.jpg)

The parts I identified on the original controller board:

- [AT91SAM7S256D-AU](https://www.microchip.com/en-us/product/AT91SAM7S256) - the MCU. ARM7TDMI, 256 KB Flash, 64 KB SRAM, 64-LQFP, on an 18.432 MHz crystal (exactly the value the PLL needs to synthesize the 48 MHz USB clock). Runs the whole show and presents the USB device port to the radio. Its logic section runs from USB VBUS at under 100 mA.
- [ADuM1410](https://www.analog.com/en/products/adum1410.html) - Analog Devices iCoupler, a 4-channel digital isolator. This is the barrier between the radio-referenced logic and the vehicle-referenced coil drive. Relay commands cross it outbound; relay coil supply power-good status comes back on a dedicated channel.
- [TPS3808G01](https://www.ti.com/product/TPS3808) - adjustable voltage supervisor in SOT-23-6. One sits on the isolated side watching the 9 V coil rail and returns a power-good signal to the MCU over an ADuM1410, in addition to a couple located on the USB side.
- [DS2433](https://www.analog.com/en/products/ds2433.html) - 4 Kb 1-Wire EEPROM. Holds the GCAI accessory ID the radio reads to decide whether to drive the port as USB or RS-232.

The coil drivers sit behind the isolators, on the controller board. They run from a 9 V rail rather than 12 V to cut coil heat dissipation. That rail is derived from A+, the high-current power input at the bus bar on the relay board, through a switcher the MCU turns on and off. A+ and its ground return reach the controller board on the 14-position board-to-board harness, so the coil supply and ground domain is entirely separate from the USB VBUS that runs the logic.

The relay board itself is entirely passive: ten relays, the fuses, terminal blocks, lugs, and the bus bar. The relays are Tyco/TE [V23201-C1001-A502](https://octopart.com/datasheet/te-connectivity/V23201C1001A502) (TE 5-1414782-7), SPST, rated 33 A at 12 V with a 40 A limiting continuous current at 23 C. Motorola derated this rating to 12 A per output behind a 15 A fuse. The coil is nominally 12 V, but must-operate is only 6.9 V, which is what lets Motorola save dissipation by running the rail at 9 V. I measured 45 mA per coil at 9 V at room temperature, consistent across all ten channels, so 0.45 A and about 4 W with everything energized.

The two boards talk to each other over a 14-position, 0.1" pitch harness.

| Pin | Assignment | Description |
|---|---|---|
| 1 | Coil common | Shared coil return for all ten channels |
| 2 | A+ | High-current vehicle input, tapped from the bus bar |
| 3-12 | Coil 1+ ... Coil 10+ | One switched coil leg per channel, high side |
| 13, 14 | GND | Relay-board-side ground |

That pinout is the whole interface, and it's simple enough that you don't strictly need a special controller board at all. Ten switched legs against a common return means a bank of ordinary panel switches feeding +9 V into pins 3 through 12 would work, with the 9 V coming from any cheap buck module.

***Note: you can't feed the coils straight off of A+.*** These are 12 V relays with a rated coil power of 818 mW, and at the datasheet's 176 ohms that rating works out to exactly 12.0 V. A vehicle's 13.8 V puts about 78 mA through each coil for 1.08 W, roughly 32% over. 

![ORC Rev A (green, right) next to the OEM PMUN1046A control PCB (blue, left), angled view](/images/ORC/side_by_side_angle.jpg)

My replacement keeps the same two-domain shape as Motorola's, with isolated logic on one side, coil drive on the other. The full [schematic is on github](https://github.com/aramder/orc/blob/main/hardware/orc.pdf) if you'd rather just read it:

- **ESP32-C3 Super Mini** - the MCU at the heart of the controller board. It handles the CAN and USB external interfaces, and controls the relays over the isolated I2C barrier.
- **[SN65HVD230](https://www.ti.com/product/SN65HVD230)** - 3.3 V CAN transceiver. Bus ESD protection is built into the part, and a 120 ohm termination resistor can be connected via a removable jumper.
- **[ADuM1250](https://www.analog.com/en/products/adum1250.html)** - hot-swappable isolated I2C buffer. This is my whole isolation barrier: instead of running ten command lines through a bank of isolator channels the way Motorola did, only SDA and SCL cross, and everything that drives the channels lives on the coil side and gets addressed over that one bus.
- **[PCA9555](https://www.nxp.com/products/PCA9555)** - 16-bit I2C GPIO expander at address 0x20, on the isolated side. Ten of its sixteen pins are the channel enables. Reading its input port back is also how the firmware reports applied state, so status comes from the hardware rather than from a variable.
- **[AO3401A](https://www.aosmd.com/sites/default/files/res/datasheets/AO3401A.pdf) x10** - the high-side switches. The relay coil returns are common on the relay board, so switching has to happen between +9 V and the top of each coil, which rules out the usual low-side sink array. Each P-FET is turned on by an MMBT3904 level shifter from an expander pin.
- **[SS34](https://www.onsemi.com/download/data-sheet/pdf/ss39-d.pdf) x10** - flyback diode. Not ideal for this to be all the way on another board, but whatever.
- **[LMR50410](https://www.ti.com/product/LMR50410) x2** - a SOT-23-6 synchronous buck used twice: once for 3.3 V logic, once for the 9 V coil rail off the harness A+ tap. Both are designed around a 28.8 V input ceiling, so the board works on a 24 V system as well as a 12 V one.
- **4-position DIP switch** - node ID, read directly by four MCU GPIOs rather than through the expander. That matters because the expander is powered from the vehicle harness: on a bench with only USB plugged in, the isolated side is dark, and the board still needs to know its own address.

Control works over either CAN or USB, from the same firmware, against the same relay state. CAN is the "correct" interface: a CANopen subset at 125 kbit/s, with an RPDO carrying a ten-bit channel mask, a TPDO reporting applied state, and a heartbeat. USB is a plain ASCII protocol over the module's CDC port, using commands like `SET 3 ON` and `STATUS`. Both paths go through the same apply function, so a change commanded over USB still shows up in the CAN status broadcast. There's a fail-safe timeout on both interfaces (longer on USB) that disables all channels if the commanding side goes quiet.

The control board uses the original alignment posts and fasteners. The original board-to-board cable mates to a shrouded 0.1" pitch male pin header, so we can just use an unshrouded header and confidently call it a day... until the PCB arrives and the through-hole pins short against the enclosure. Some lead trimming and liberal Kapton tape application allow for a clean (enough) fit in the PMUN1046A's gorgeous cast enclosure.

![ORC Rev A PCB alone in the PMUN1046A enclosure, showing the CAN bus screw terminal, DIP address switches, and USB-C programming port](/images/ORC/ORC_in_PMUN1046A.jpg){: style="width: 60%; display: block; margin: 0 auto;"}

The source for this project, both the firmware and hardware, is available on github at [aramder/orc](https://github.com/aramder/orc).

At the time of writing this article, I have a few of these PCBs which I don't have an immediate use for. Feel free to drop me a line if you're interested in one (email at the bottom of the page).
