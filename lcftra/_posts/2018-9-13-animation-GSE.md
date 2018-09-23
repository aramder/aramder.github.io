---
layout: post
category: lcftra
title: Animation System GSE
---
![Photo of control panel](/images/lcftra/GSE/panel assembled.jpg)

Testing, calibrating, and programming of the animation system requires some support hardware. The system uses several communications busses, as well as several hardware enable and status lines.<!--more-->

![Assembled main PCBA](/images/lcftra/GSE/main PCBA.jpg)

This piece of GSE is capable of supplying individual <a href="https://aramder.github.io/animation-bank-module/" target="_blank">valve bank boxes</a> with the control signals needed to either emulate a connection to the <a href="https://aramder.github.io/animation-computer/" target="_blank">main computer</a>, as well as interface a valve bank module with a PC for testing purposes. For more information about how the various pieces of the animation system interface with one another, check out <a href="https://aramder.github.io/animation-summary/" target="_blank">this summary</a> of the new animation system.

![Assembled layered PCBAs mounted to underside of the panel](/images/lcftra/GSE/underside with PCBA.jpg)

This unit is essentially a glorified USB to serial converter. The main PCB consists of a quad USB to serial converter, and several transceivers. The Gilderfluke Br-EFB requires RS-422 for configuration, and uses DMX-512 (a specific RS-485 protocol) for command data. An additional RS-485 transceiver was included for a future hydraulic system monitoring project.

![Underside of panel, wired](/images/lcftra/GSE/panel underside.jpg)

Aside from handling data, the GSE also provides various enable signals for the valve bank module electronics. Each channel's hydraulic vavle driver, as well as the Br-EFB (the PID controller for all 4 channels in each bank), has an indiviudal enable. There is also a port for a remote e-stop button which must be connected in order to enable anything in the valve bank box.

![Photo of GSE and remote e-stop](/images/lcftra/GSE/GSE and Estop.jpg)

With the completion of this unit we are now ready to test the functionality of the animation system. My goal is to have the system functioning by Oct 6th for our T1 inspection.

![External photo of GSE enclosure](/images/lcftra/GSE/enclosure external.jpg)

