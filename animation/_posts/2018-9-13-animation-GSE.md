---
layout: post
category: animation
title: Animation System GSE
---
![Front panel of the GSE unit with connectors and switches for testing valve bank modules](/images/GSE/panel assembled.jpg)

Testing, calibrating, and programming of the La Cañada Flintridge float's animation system requires some support hardware. The system uses several communications busses, as well as several hardware enable and status lines which all need to be accessed for programming.<!--more-->

![Main GSE PCB featuring USB-to-serial converters and RS-422/RS-485 transceivers](/images/GSE/main PCBA.jpg)

This piece of GSE is capable of supplying individual <a href="https://aramder.github.io/animation-bank-module/">valve bank boxes</a> with the control signals needed to either emulate a connection to the <a href="https://aramder.github.io/animation-computer/">main computer</a>, as well as interface a valve bank module with a PC for testing purposes. For more information about how the various pieces of the animation system interface with one another, check out <a href="https://aramder.github.io/animation-summary/">this summary</a> of the new animation system.

![PCBAs mounted to the underside of the front panel](/images/GSE/underside with PCBA.jpg)

This unit is essentially a glorified USB to serial converter. The main PCB consists of a quad USB to serial converter, and several transceivers. The Gilderfluke Br-EFB requires RS-422 for configuration, and uses DMX-512 (a specific RS-485 protocol) for command data. An additional RS-485 transceiver was included for a future hydraulic system monitoring project.

![Wiring on the underside of the panel connecting enable switches to the PCBAs](/images/GSE/panel underside.jpg)

Aside from handling data, the GSE also provides various enable signals for the valve bank module electronics. Each channel's hydraulic vavle driver, as well as the Br-EFB (the PID controller for all 4 channels in each bank), has an indiviudal enable. 

![GSE unit alongside the required remote emergency stop button](/images/GSE/GSE and Estop.jpg)

There is also a port for a remote e-stop button which must be connected in order to enable anything in the valve bank box.

![Completed GSE unit in its portable enclosure](/images/GSE/enclosure external.jpg)

The animation system has since successfully been down the parade route! The float, Tree Frog Night, featured 3 frog musicians and an accompanying cast of dancing fish. For an overview of the animation system's debut, check out <a href="https://aramder.github.io/animation-2019/">this page</a>.
