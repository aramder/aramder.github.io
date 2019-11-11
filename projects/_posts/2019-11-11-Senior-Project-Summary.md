---
layout: post
category: projects
title: Senior Project Summary
---
![A rendering with 2 printed circuit boards inside a plastic enclosure](/images/projects/Senior Project/addressable LED module render side.png)

For my senior project, I'm working on an embedded lighting controller which is being designed to provide flexible lighting control/drive in an extremely flexible and compact package. <!--more-->

The Embedded Lighting Controller is a product meant to allow both hobbyists and professionals to add lighting in a variety of applications ranging from costumes to theatrical props. Lighting is a critical element of performance art, either contributing to a visual art performance or display, or by helping visualize a non-visual medium such as music. Between theatre sets, props, costumes and even parades, lighting is used to great effect, with some shows such as Disney’s World of Color essentially just consisting of lighting, music, and water effects.

We hope to improve on existing lighting controllers/drivers by making the Embedded Lighting Controller easy to setup and integrate with existing show control systems, and compact for ease of embedding the device in finished products. By allowing the unit to run animations using internally stored data or connect to external show control systems, and by having modular output boards for driving different kinds of lights, we hope to provide an extremely versatile lighting controller.

![A sketch showing the top motherboard PCB and the two lower daughterboard PCB modules](/images/projects/Senior Project/modular construction sketch.png)

The compact unit, which we're currently trying to build into a 3.3 in x 2.2 in x 0.9 in enclosure, will be capable of being controlled by lighting industry standards such as DMX512-A, ArtNet, or sACN. We also plan to be able to read show control data from an SD card for easy stand-alone operation or use as an independant show controller.

![A second rendering with 2 printed circuit boards inside a plastic enclosure viewed from above](/images/projects/Senior Project/addressable LED module render top.png)

We plan to have a mother/daughter board configuration that will allow for different driver PCB assemblies to be installed. For now, we are planning on one module to support addressable RGB(W) LED tape (multiple protocols), and basic PWM MOSFET for switching regular RGBW LED tape or other misc. lighting loads.
