---
layout: post
category: lcftra
title: Animation System Main Computer
---
![A picture of the unit's internal electronics](/images/lcftra/animation computer/enclosure external.jpg)

The new La Cañada Flintridge rose parade float's animation system has a controller unlike anything used in the parade. The  custom controller has a 12 inch waterproof industrial grade touchscreen that sports a custom control GUI and convenient networking capabilities.<!--more-->

The animation computer contains the main show controller and various support hardware. The "animation computer" hasn't traditionally used what we would think of as a computer, but has rather been an assembly of custom or commerical off-the-shelf industrial control hardware (at least in the case of the La Cañada float). This animation computer actually contains a computer, however, it only serves to control dedicated show control hardware. To see how the main computer fits in to the animation system, check out <a href="https://aramder.github.io/animation-summary/" target="_blank">this summary</a> of the new animation system.

At the heart of the system is a controller/inerfacing PCB assembly. This board is responsible for controlling the main Gilderfluke Sd-50/40 show controller, as well as interfacing with the four Br-EFB PID controllers and 16 Rexroth proportional valve drivers.

<img class="shrunk" src="/images/lcftra/animation computer/controller PCBA.jpg" alt="The assembled controller PCB in an assembly stand">

The PCBA consists of 20 relays (which serve as a manual backup), connectors for power, the Sd-50/40, and each valve bank box, and a 5 volt power supply for the Raspberry Pi which runs the controller via the GUI.

![The touchscreen sitting on a lab bench next to the controller interface PCBA and raspberry pi](/images/lcftra/animation computer/touchscreen development.jpg)

The GUI, written in Python, allows the animation operator to control the Sd-50/40 show controller, enable/disable each valve driver individually, as well as provide a health status for each Br-EFB. The GUI has a number of customizable parameters to aid the animation operator such as configurable labels (descriptive names instead of channel numbers), quick device configuration loading, and more.

<img class="shrunk" src="/images/lcftra/animation computer/electronics full.jpg" alt="A look inside the animation computer - the inside of the LCD can be seen on the lid of the enclosure, as well as the electronics in the bottom half">

![A look inside the animation computer - just the lower half, filled with electronics](/images/lcftra/animation computer/electronics lower half.jpg)

![The empty enclosure covered in blue tape for painting the inside lip of the enclosure's cutouts](/images/lcftra/animation computer/enclosure painting.jpg)


