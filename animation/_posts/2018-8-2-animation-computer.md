---
layout: post
category: animation
title: Animation System Main Computer
---
![A picture of the unit's internal electronics](/images/animation computer/enclosure external.jpg)

The new La Cañada Flintridge Rose Parade float's animation system has a controller unlike anything used in the parade. The custom controller has a 12 inch waterproof touchscreen that sports a custom control GUI and convenient system configuration capabilities.<!--more-->

The animation computer contains the main show controller and various support hardware. The "animation computer" hasn't traditionally used what we would think of as a computer, but has rather been an assembly of custom or commerical off-the-shelf industrial control hardware (at least in the case of the La Cañada float). This animation computer actually contains a computer, however, it only serves to control dedicated show control hardware. To see how the main computer fits in to the animation system, check out <a href="https://aramder.github.io/animation-summary/">this summary</a> of the new animation system.

At the heart of the system is a controller/inerfacing PCB assembly. This board is responsible for controlling the main Gilderfluke Sd-50/40 show controller, as well as interfacing with the four Br-EFB PID controllers and 16 Rexroth proportional valve drivers.

<img class="shrunk" src="/images/animation computer/controller PCBA.jpg" alt="The assembled controller PCB in an assembly stand">

The PCBA consists of 20 relays (with manual actuation tabs which serve as a manual backup), connectors for power, the Sd-50/40, and each valve bank box, as well as a 5 volt power supply for the Raspberry Pi which runs the controller via the GUI.

![The touchscreen sitting on a lab bench next to the controller interface PCBA and raspberry pi](/images/animation computer/touchscreen development.jpg)

The GUI, written in Python, allows the animation operator to control the Sd-50/40 show controller, enable/disable each valve driver individually, as well as provide a health status for each Br-EFB. The GUI has a number of customizable parameters to aid the animation operator such as configurable labels (descriptive names instead of channel numbers), customizable device configuration loading, and more.

Now of course all of this has to be packaged in a suitable enclosure. Just like the <a href="https://aramder.github.io/animation-bank-module/">valve bank modules</a>, the connectors on the box will be mounted on powder-coated custom waterjet cut plates. Three large rectangular openings were cut in the animation controller box for the two connector plates and the touchscreen. The exposed metal on all of the boxes was painted with matching ANSI 61 gray paint.

![The empty enclosure covered in blue tape for painting the inside lip of the enclosure's cutouts](/images/animation computer/enclosure painting.jpg)

The touchscreen, emergency stop button, and power switch actuator are mounted to the lid of the enclosure. The system's power switch functions as a safety lockout; the unit can not be opened while power is on. The switch also accommodates three lockout-tagout locks which prevent the controller from being turned on or opened.

![Assembling the back panel which secures all of the electronics](/images/animation computer/panel assembly.jpg)

The lower half of the animation computer contains several power supplies, the Gilderfluke Sd-50/40 show controller, the Raspberry Pi and controller/interface PCBA, router, and DC distribution hardware.

![A look inside the animation computer - just the lower half, filled with electronics](/images/animation computer/bottom half lit.jpg)

Yes, I know what you're thinking; that does look awfully compact. We could have chosen a larger enclosure, but since this unit has to be installed in potentially small crew compartments and must be easy to install and remove, we decided to go with as cozy of an enclosure as possible.

<img class="shrunk" src="/images/animation computer/main controller open.jpg" alt="A look inside the animation computer - the inside of the touchscreen can be seen on the lid of the enclosure, as well as the electronics in the bottom half">

The animation system has since successfully been down the parade route! The float, Tree Frog Night, featured 3 frog musicians and an accompanying cast of dancing fish. For an overview of the animation system's debut, check out <a href="https://aramder.github.io/animation-2019/">this page</a>.

