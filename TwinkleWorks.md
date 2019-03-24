---
layout: page
title:
permalink: /TwinkleWorks/
---
![TwinkleWorks logo](/images/TwinkleWorks/twinkleworks w background.png)

# Disclaimer

This page is here to provide some information about TwinkleWorks, as TwinkleWorks does not have an official public facing website. These products and projects are only shown to provide context for my work at AES/TwinkleWorks and not for official reference.

# Background

TwinkleWorks is a subsidiary of <a href="http://www.aescreative.com/" target="_blank">Artistic Entertainment Services</a> that specializes in LED strobe lighting.

TwinkleWorks has several lines of LED strobe fixtures in various sizes and colors, made for a variety of scenic lighting applications.

Twinkleworks also produces several LED drivers. Currently manufactured drivers include:

![TwinkleWorks ED32](/images/TwinkleWorks/ED32.jpg)

ED32 - 32 channel DMX controlled rack mount LED driver

![TwinkleWorks LEDPS](/images/TwinkleWorks/LEDPS.jpg)

LEDPS - 24 channel random sparkle stand-alone LED driver

# Developments

## RGBW Strobe

During my time at TwinkleWorks, we began development of a RGBW strobe fixture. I developed the new PCBA used in each fixture and worked with a local manufacturer to setup procedures for manufacturing (pending successful testing). When I left, this product was currently entering a rigorous testing phase.

![CAD mockup of RGBW strobe fixture](/images/TwinkleWorks/RGBW side view.png)

This strobe is currently undergoing testing before being released for production. A work in progress datasheet can be found 
<a href="https://aramder.github.io/images/TwinkleWorks/RGBW Strobe Spec Sheet [NOT FINAL].pdf" target="_blank">here</a>. Please note that this datasheet is not final and is only for reference.

## ED128

We also began developing a new LED driver, referred to as the ED128 or EDRGB. The driver will be capable of driving 128 individual, or 32 RGBW, LED fixtures. Each of the 128 channels will feature temperature compensation and be capable of driving LEDs at 0.7A at up to 34v. 

Some quick math should tell you we’re talking about some serious power. Though this seems like a big issue at first, TwinkleWorks fixtures are only designed to handle the thermal dissipation required for a strobing LED, meaning the controller will not have a very heavy duty cycle due to output regulation.
