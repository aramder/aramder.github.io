---
layout: post
category: misadventures
title: Custom Boot Logos on the PMR-171
---

![PMR-171 displaying a custom boot logo](/images/PMR171/boot_logo_tool/pmr171_are_belong_to_us.jpg)

The PMR-171 (and all its Guohetec siblings) display a small 100x100 pixel logo on a simple background when they boot. I wanted to replace it with a full-screen image. The result is an open-source Python tool that takes any image and produces a ready-to-flash firmware file. No debug probe required.<!--more-->

## Finding the Boot Logo

The radio runs on an STM32H743IIT6 (Cortex-M7, 2 MB flash). Starting from a full flash dump pulled over JTAG with a J-Link, a string search located `SEGGER emWin V5.44.70` in the binary. That identifies the GUI library as STemWin (ST's distribution of SEGGER emWin). emWin stores bitmaps with a 20-byte `GUI_BITMAP` header, so a scan for valid bitmap descriptors (reasonable width/height, valid stride, data pointer within flash range) identified 37 bitmaps in the firmware: icons, status indicators, and three boot logos, one per model variant.

<div style="max-width: 50%; margin: 0 auto;">
{% include gallery.html
   images="/images/PMR171/boot_logo_tool/stock_logo_pmr171.png, /images/PMR171/boot_logo_tool/stock_logo_hs2.png, /images/PMR171/boot_logo_tool/stock_logo_qr20.png"
   alts="PMR-171, HS2, QR20"
   cols="3"
   group="stock-logos" %}
</div>

The PMR-171's logo is stored at `0x08108CC8` as 100x100 pixels in RGB565 (16-bit, little-endian, 2 bytes per pixel). All three model-variant logos live in flash sector 8.

<!-- TODO: Photo of the stock boot screen on the actual radio (before patching).
     Destination: /images/PMR171/boot_logo_tool/photo_stock_boot.jpg
     Source images dir: c:\Users\Aram\Documents\GitHub\aramder.github.io\images\PMR171\boot_logo_tool\
-->

## Splash Screen Function

The boot splash function at `0x080904D4` reads a model index byte from EEPROM and switches on it to select the logo address, draw coordinates, text overlay string, and background color. For the PMR-171 (case 6): bitmap at `0x08108CC8`, drawn at (110, 50), with "PMR-171" rendered below.

The bitmap address isn't encoded directly in an instruction. It's loaded from a *literal pool* via `ldr r0, [pc, #offset]` (ARM Thumb-2 can't fit a 32-bit address into a 16-bit instruction, so the address is stored in a nearby data table and loaded indirectly). Changing 4 bytes in the literal pool redirects the function to a different bitmap.

The patching strategy:

1. Write a new full-screen image into an unused flash sector
2. Overwrite the 4-byte pointer in the literal pool to point at the new image
3. Set the X/Y draw coordinates to (0, 0) instead of (110, 50)
4. Optionally NOP the `bl` instructions that draw the model name and version text

About 13 bytes of actual code/data changes, plus the image pixel data.

## Pixel Format

The LCD is an ST7789V on SPI2 at 6.25 MHz, configured for 320x240 landscape (MADCTL `0x60`, pixel format `0x3A = 0x05`). emWin uses `LCD_Color2Index_RGB565` / `LCD_Index2Color_RGB565` for color conversion. Bitmaps are stored as 16-bit RGB565 pixels (5R/6G/5B), little-endian.

A full-screen 320x240 image: 153,600 bytes of pixel data + 20-byte emWin header = 153,620 bytes (~150 KB). The STM32H7's Bank 2 sectors are 128 KB each. Sectors 10 through 13 are erased in stock firmware, so there's room for a full-screen image with space to spare.

## From Debug Probe to USB Stick

The initial workflow required JTAG: dump firmware, patch, flash back. The PMR-171 has a simpler path. Its bootloader (UHSDR-derived) checks for `FW-NEW.bin` on a FAT32 USB stick at power-on. If found, it erases Bank 2 and programs the file starting at `0x08020000`.

The OEM distributes firmware updates in exactly this format: Bank 2 contents only, trailing `0xFF` trimmed, no header or checksum. The tool uses the same file as its input:

1. Read the OEM `FW-NEW.bin` (~1.1 MB)
2. Reconstruct a full 2 MB flash image internally (pad with `0xFF`)
3. Apply patches
4. Extract Bank 2, trim, write as a new `FW-NEW.bin`

The user downloads the OEM firmware, runs the tool, copies the output to a USB stick, and powers on.

<!-- TODO: Photo of the USB stick in the radio, or the radio mid-flash.
     Destination: /images/PMR171/boot_logo_tool/photo_usb_update.jpg
     Source images dir: c:\Users\Aram\Documents\GitHub\aramder.github.io\images\PMR171\boot_logo_tool\
-->

## The Tool

[pmr171-logo-tool](https://github.com/aramder/pmr171-logo-tool) is a Python CLI that handles the pipeline: image resize/convert, emWin header generation, binary patching, FW-NEW.bin output.

```
python cli.py patch mylogo.png --no-text
```

Accepts PNG, JPEG, BMP, etc. Resizes to 320x240 (letterbox, crop-to-fill, or stretch modes), converts to BGR565, builds the emWin bitmap header, patches the firmware, and writes a USB update file.

`--no-text` NOPs the branch-and-link instructions that render the model name and version string over the boot image.

![PMR-171 displaying a custom boot screen with name and callsign](/images/PMR171/boot_logo_tool/pmr171_my_boot.jpg)

## One Firmware to Rule Them All

Guohetec sells at least eight models on this platform: Q900, HS2, QR20, TBR-119, PMR-119, SJR-188, PMR-171, and MX-1000. All run the same firmware binary. The model is selected by an EEPROM index byte. Differences are limited to Bluetooth name, band-switching tables, IMU orientation, and on-screen branding. Flash layout, LCD, emWin, and boot logo mechanism are identical across all of them.

The tool supports all eight models. A `--universal` flag injects a small Thumb-2 stub that replaces the model-index switch entirely, drawing the custom image at (0, 0) regardless of which EEPROM index the radio reads. One patched `FW-NEW.bin` works on any Guohetec radio on this platform.

## Version Compatibility

The patch offsets are hard-coded for firmware v3.7.2 (build `Dec 22 2025 09:25:53`). A different firmware version will have different code layout, and applying these patches to it will produce a corrupted image. In most cases the radio can be recovered by USB-flashing a known-good `FW-NEW.bin`, but there is no guarantee that a corrupted firmware won't damage the bootloader or leave the radio in a state that requires JTAG recovery. Do not use this tool on a firmware version other than v3.7.2 unless you have a JTAG debug probe and are prepared to use it.

The tool is available at [github.com/aramder/pmr171-logo-tool](https://github.com/aramder/pmr171-logo-tool).

*Disclosure: both the reverse engineering and this writeup were done with heavy AI assistance. I directed the investigation, provided the hardware and JTAG dumps, and verified results on the physical radio. The LLM handled disassembly analysis, script writing, pattern matching through the binary, and drafting this post. There may be mistakes, misunderstandings, or inaccuracies in the technical details.*
