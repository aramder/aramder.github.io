---
layout: post
category: lcftra
title: Animation System Revamp Summary
---
![A picture of the original animation system](/images/lcftra/original system.jpg)

As of 2018, the La Cañada Fltintridge rose parade float's animation system is nearly 20 years old. As the system continues to age, components that are no longer manufactured are slowly beginning to fail. Starting in 2017, I began work on a replacement.<!--more-->

![A block diagram of the original animation system closed loop feedback control system](/images/lcftra/original system diagram.png )

The original system is based of off Rexroth hydraulic control systems interfaced with Gilderfluke show controls. The Gilderfluke Sd-50/40 is responsible for providing synchronized position data as well as audio for the float's sound system. The position data is sent to a Rexroth valve driver module which then actuates hydraulic valves to move various animation mechanisms on the float.

![A block diagram of the new system's main controller](/images/lcftra/control box diagram.png)

The system has been redesigned to operate using the same Gilderfluke Sd-50/40 for overall animation show control, but there are rather drastic changes to the user interface and the way the system is divided. Unlike the previous animation system, the unit is broken in to 5 boxes, a single main control unit, and 4 seperate "valve bank modules". The main controller is kept in the animator's compartment on the float, and is linked to each of the valve bank modules which can be mounted wherever they're needed on the float. 

![A block diagram of the new system's individual valve bank controllers](/images/lcftra/valve module diagram.png)

The new animation system functions in a somewhat similar manner to the old one, though responsibilities are shared slightly differenctly between the Rexroth and Gilderfluke systems. In this system, closed loop control functions are carried out using a Gilderfluke Br-EFBp; the Rexroth valve driver modules only serve to amplify the control signals from the Br-EFB.

![A picture of the main controller's interfacing PCBA](/images/lcftra/controller PCBA.jpg)

A much more significant update to the animation system is the user interface. Instead of a box with quite literally over a hundered switches, the system will be controlled by a computer that interfaces with hardware through a custom designed PCB.

![A picture of a large touchscreen with a custom GUI](/images/lcftra/controller GUI.jpg)

The animation computer will be controlled using this 12" waterproof touchscreen. The integration of a touchscreen and computer into the system not only allows for a simplified user interface, but also allows for testing, debugging, and calibration of the system without an external computer.
