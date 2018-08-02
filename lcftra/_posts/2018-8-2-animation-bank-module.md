---
layout: post
category: lcftra
title: Animation System Valve Bank Module
---
![A picture of the unit's internal electronics](/images/lcftra/bank module/internal electronics.jpg)

The new La Cañada Flintridge rose parade float's animation system is built in several modular pieces. Four of these units will be responsible for controlling a bank of four hydraulic animation channels.<!--more-->

The valve bank control modules each contain a PID controller, and drivers for the hydraulic valves. To see how this unit fits in to the animation system, check out <a href="https://aramder.github.io/animation-summary/">this summary</a> of the new animation system.

These modules mostly contain commercial off-the-shelf parts, such as the Gilderfluke Br-EFB PID controller and Rexroth valve drivers, but some parts were custom built.

The system uses a variety of connectors such as circular MIL spec connectors, D-subs, and various other data and audio connectors. The system has 30 circular MIL spec connectors, which require 150 rather precisely drilled holes. Some parts, like our D-sub, ethernet, and USB connectors need oddly shaped holes which would require machining. Our solution was to draw the layout of the connectors in CAD, and have thin plates, as well as accompanying gaskets, made.

![A flat piece of gasket material placed in a laser cutter](/images/lcftra/bank module/unpainted panel.jpg)

The plates for the connectors where cut on a waterjet, courtesy of Ben Baral and the Harvey Mudd machine shop.

![A flat piece of gasket material placed in a laser cutter](/images/lcftra/bank module/gasket cutting.jpg)

Gaskets for the plates were also laser cut courtesy of Ben Baral.

![A picture of the bottom of the enclosure, all connectors are visible](/images/lcftra/bank module/enclosure connectors.jpg)

The plates were powder-coated to match the powder-coating of our Hoffman industrial enclosures.

Another custom part of our system is a quad 18 volt power supply in each valve bank module. The Gilderfluke Br-EFB outputs 24v, 10v, and -10v (unused), which is adequate to power all modern position sensors, however, to maintain backwards compatibility with our older position sensors we need an 18v supply.

![Four custom designed and built power supplies](/images/lcftra/bank module/18v power supplies.jpg)
The PCB assembly isn’t very complicated, consisting of a linear voltage regulator and PTC fuses.

<img class="shrunk" src="/images/lcftra/bank module/mounted power supply.jpg" alt="One of the power supplies mounted to the lid of the enclosure">

These power supplies are mounted on the lid of the enclosure. Though they will not need to dissipate a great deal of heat, they are in close contact with the wall of the enclosure, and thermal paste will assist in dissipating heat through the enclosure’s large surface area.
