---
layout: post
category: lcftra
title: Animation System Main Computer
---
![A picture of the unit's internal electronics](/images/lcftra/animation computer/enclosure external.jpg)

The new La Cañada Flintridge rose parade float's animation system has a controller unlike anything used in the parade. The  custom controller has a 12 inch waterproof touchscreen that sports a custom control GUI and convenient networking capabilities.<!--more-->

The animation computer contains the main show controller and various support hardware. The "animation computer" hasn't traditionally used what we would think of as a computer, but has rather been an assembly of custom or commerical off-the-shelf industrial control hardware (at least in the case of the La Cañada float). This animation computer actually contains a computer, however, it only serves to control dedicated show control hardware. To see how the main computer fits in to the animation system, check out <a href="https://aramder.github.io/animation-summary/" target="_blank">this summary</a> of the new animation system.

At the heart of the system is a controller/inerfacing PCB assembly. This board is responsible for controlling the main Gilderfluke Sd-50/40 show controller, as well as interfacing with the four Br-EFB PID controllers and 16 Rexroth proportional valve drivers.

<img class="shrunk" src="/images/lcftra/animation computer/controller PCBA.jpg" alt="The assembled controller PCB in an assembly stand">

The PCBA consists of 20 relays (with manual actuation tabs which serve as a manual backup), connectors for power, the Sd-50/40, and each valve bank box, as well as a 5 volt power supply for the Raspberry Pi which runs the controller via the GUI.

![The touchscreen sitting on a lab bench next to the controller interface PCBA and raspberry pi](/images/lcftra/animation computer/touchscreen development.jpg)

The GUI, written in Python, allows the animation operator to control the Sd-50/40 show controller, enable/disable each valve driver individually, as well as provide a health status for each Br-EFB. The GUI has a number of customizable parameters to aid the animation operator such as configurable labels (descriptive names instead of channel numbers), customizable device configuration loading, and more.

Now of course all of this has to be packaged in a suitable enclosure. Just like the <a href="https://aramder.github.io/animation-bank-module/" target="_blank">valve bank modules</a>, the connectors on the box will be mounted on powder-coated custom waterjet cut plates. Three large rectangular openings were cut in the animation controller box for the two connector plates and the touchscreen. The exposed metal on all of the boxes was painted with matching ANSI 61 gray paint.

![The empty enclosure covered in blue tape for painting the inside lip of the enclosure's cutouts](/images/lcftra/animation computer/enclosure painting.jpg)

**Pictures and descriptions below are for work that is currently in progress**

The touchscreen, emergency stop button, and power switch actuator are mounted to the lid of the enclosure. The system's power switch functions as a safety lockout; the unit can not be opened while power is on. The switch also accomodates three lockout-tagout locks which prevent the controller from being turned on or opened.

<img class="shrunk" src="/images/lcftra/animation computer/electronics full.jpg" alt="A look inside the animation computer - the inside of the touchscreen can be seen on the lid of the enclosure, as well as the electronics in the bottom half">

The lower half of the animation computer contains several power supplies, Gilderfluke Sd-50/40, the Raspberry Pi and controller/interface PCBA, router, and DC distribution hardware. Yes, I know what you're thinking; that does look awfully compact. We could have chosen a larger enclosure, but since this unit has to be installed in potentially small crew compartments and must be easy to install and remove, we decided to go with a cozy little enclosure.

![A look inside the animation computer - just the lower half, filled with electronics](/images/lcftra/animation computer/electronics lower half.jpg)

The panduit shown in these photos is not cut to length properly, and has already been replaced. Some minor components are not shown, and most notably the two plates on the sides of the enclosure are missing.

Finishing the animation computer is currently the highest priority on the animation system to-do list. The system is currently on schedule to be partially functional by late August, and fully functional by September. The system will make its debut in the 2019 Rose Parade on our float, Tree Frog Night.