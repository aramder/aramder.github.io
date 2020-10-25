---
layout: post
category: projects
title: Embedded Lighting Controller Summary
---
![A rendering with multiple printed circuit boards inside a plastic enclosure](/images/projects/ELC/motherboard top.png)

For my senior project, I'm working on an embeddable lighting controller, with the creative working title of Embedded Lighting Controller, which is being designed to provide flexible lighting control/drive in an extremely compact package. <!--more-->

The Embedded Lighting Controller is a product meant to allow both hobbyists and professionals to add lighting in a variety of applications ranging from costumes to theatrical props. Lighting is a critical element of performance art, either contributing to a visual art performance or display, or by helping visualize a non-visual medium such as music. Between theatre sets, props, costumes and even parades, lighting is used to great effect, with some shows such as Disney’s World of Color essentially just consisting of lighting, music, and water effects.

Our team, comprising of <a href="https://ryansw.com/" target="_blank">Ryan White</a> and myself, hopes to improve on existing lighting controllers/drivers by making the Embedded Lighting Controller easy to setup and integrate with existing show control systems, and compact for ease of embedding the device in finished products. By allowing the unit to run animations using internally stored data or connect to external show control systems, and by having modular output boards for driving different kinds of lights, we hope to provide an extremely versatile lighting controller.

We plan to have a mother/daughter board configuration that will allow for different driver PCB assemblies to be installed. The motherboard is responsible for show control and the web interface which will be used for device configuration. In addition to providing a physical interface for DMX512-A, the motherboard will also provide a vibrator power output and a limited synthesized audio output for queuing performers if the unit is used in a costume application. The daughterboards will be responsible for translating show control data from the motherboard into the relevant output format (addressable LED signals, PWM for switching, etc.).

![A sketch showing the top motherboard PCB and the two lower daughterboard PCB modules](/images/projects/ELC/modular construction sketch.png)

The sketch above shows our original concept for the unit, comprising of a controller motherboard and two output modules. We've since changed the design slightly by removing the LCD user interface and consolidating motherboard I/O to a single connector.

![A second rendering with the assembled unit showing the various connections on two sides of the unit](/images/projects/ELC/motherboard connectors.png)

The compact unit, which is contained in a 3.3 in x 2.2 in x 0.9 in enclosure, will be capable of being controlled by lighting industry standards such as DMX512-A, ArtNet, or sACN. We also plan to be able to read show control data from an SD card for easy stand-alone operation or use as an independent show controller.

![A rendering with 2 light output modules inside a plastic enclosure viewed from above](/images/projects/ELC/addrLED and 4ChanPWM modules.png)

For now, we are planning on an addressable RGB(W) LED tape (multiple protocols) module (right), and basic PWM MOSFET module for switching regular RGBW LED tape or other misc. lighting loads (left). In the future, we hope to add additional modules for added flexibility in lighting or show control systems such as RC servo outputs, audio playback, and more.

**Update** - *April 2020* - The boards have all been tested and are functional. Firmware development is proceeding.

![Motherboard connected to small LiPo battery with various indicator LEDs active](/images/projects/ELC/motherboard functional.jpg)
