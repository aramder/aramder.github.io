---
layout: post
category: misadventures
title: VGA to Oscilloscope (XYZ) Converter
---
![My profile photo displayed on an oscilloscope via the VGA converter](/images/vga to oscope/profile full.jpg)

A few years ago, I built some hardware to allow an oscilloscope to be used as a VGA display. I often use the photo above as my profile/avatar online and get asked why there are crosshairs on me... here's how it works!<!--more-->

![VGA to oscilloscope converter in a die-cast metal enclosure](/images/vga to oscope/vga to oscope converter.jpg)

Not to delve too far into the VGA signalling standard, but it's essentially meant to drive cathode ray tube (CRT) monitors in as simple of a way as possible using a few analog and digital signals. A VGA monitor receives a set of horizontal and vertical synchronization pulses which are used to drive the electron beam across the screen in order to draw the desired image, while red, green, and blue analog signals control the display of colors as the beam makes its way along the screen. The circuitry needed to parse the VGA signals and control a basic CRT like that of an old oscilloscope can be implemented with a few basic ICs.

![Internal view showing op-amps and 555 timers on perfboard](/images/vga to oscope/vga to oscope internal.jpg)

The photo above shows the relatively simple circuit implementation using a handful of op-amps and 555 timer ICs. The original circuit comes from Jon Stanley's <a href="https://www.electronixandmore.com/vgatoscope/index.html">fantastic site</a> which has a plethora of interesting and very well documented electronics projects.

![Converter panel with power banana jacks and BNC outputs for X, Y, Z](/images/vga to oscope/vga to oscope panel.jpg)

Was this a waste of my time?

![Roger Sterling saying "who cares?"](/images/vga to oscope/who cares.jpg)
