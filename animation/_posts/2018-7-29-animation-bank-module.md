---
layout: post
category: animation
title: Animation System Valve Bank Module
---
![A picture of the unit's internal electronics](/images/bank module/internal electronics.jpg)

The new La Cañada Flintridge rose parade float's animation system is built in several modular pieces. Four identical units will be valve bank modules, which are responsible for controlling a bank of four hydraulic animation channels.<!--more-->

The valve bank control modules each contain a PID controller, and drivers for the hydraulic valves. To see how this unit fits in to the animation system, check out <a href="https://aramder.github.io/animation-summary/">this summary</a> of the new animation system.

These modules mostly contain commercial off-the-shelf parts, such as the Gilderfluke Br-EFB PID controller and Rexroth valve drivers, but some parts of the system were custom built.

Previously, all of our boxes had openings for connectors, buttons, switches, gauges, etc. drilled by hand, but for the new animation system we took a different approach. We drew the layout of the connectors in CAD, and had thin metal plates, as well as accompanying gaskets, made. This saved us countless hours of machining work. Though waterjeting plates for a purpose like this isn’t exactly revolutionary, we were rather relieved to find an elegant and time saving alternative to drilling and machining just over 200 holes and openings by hand.

![A flat piece of gasket material placed in a laser cutter](/images/bank module/unpainted panel.jpg)

The plates for the connectors where cut on a waterjet, courtesy of Ben Baral and Paul Stovall of the Harvey Mudd machine shop.

![A flat piece of gasket material placed in a laser cutter](/images/bank module/gasket cutting.jpg)

Gaskets for the plates were also laser cut courtesy of Ben Baral.

![A picture of the bottom of the enclosure, all connectors are visible](/images/bank module/enclosure connectors.jpg)

The plates were powder-coated to match the powder-coating of our Hoffman enclosures. The d-sub is missing its waterproof cover in this photo.

Another custom part of our system is a quad 18 volt power supply in each valve bank module. The Gilderfluke Br-EFB outputs 24v, 10v, and -10v (unused), which is more than adequate for powering most position feedback sensors, however, to maintain backwards compatibility with our older position sensors we need an 18v supply.

![Four custom designed and built power supplies](/images/bank module/18v power supplies.jpg)

The PCB assembly isn’t very complicated, consisting of linear voltage regulators and PTC fuses.

<img class="shrunk" src="/images/bank module/mounted power supply.jpg" alt="One of the power supplies mounted to the lid of the enclosure">

These power supplies are mounted on the lid of the enclosure. Though they will not need to dissipate a great deal of heat, they are in close contact with the wall of the enclosure, and thermal paste will assist in dissipating heat through the lid's large surface area. 

![One of the completed bank modules mounted in the float](/images/bank module/installed bank module.jpg)

The animation system has since successfully been down the parade route! The float, Tree Frog Night, featured 3 frog musicians and an accompanying cast of dancing fish. For an overview of the animation system's debut, check out <a href="https://aramder.github.io/animation-2019/">this page</a>.
