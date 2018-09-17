---
layout: post
category: lcftra
title: Animation System GSE
---
![External photo of GSE enclosure](/images/lcftra/GSE/enclosure external.jpg)

For testing and calibrating the animation system some Ground Support Equipment (GSE) is required.<!--more-->

This piece of GSE is capable of supplying individual <a href="https://aramder.github.io/animation-bank-module/" target="_blank">valve bank boxes</a> with the control signals needed to either emulate a connection to the <a href="https://aramder.github.io/animation-computer/" target="_blank">main computer</a>, as well as interface a valve bank module with a PC for testing purposes. For more information about how the various pieces of the animation system interface with one another, check out <a href="https://aramder.github.io/animation-summary/" target="_blank">this summary</a> of the new animation system.

![External photo of GSE enclosure](/images/lcftra/GSE/main PCBA.jpg)

This unit is essentially a glorified USB to serial converter. The main PCB consists of a quad USB to serial converter, and several transceivers. The Gilderfluke Br-EFB requires RS-422 for configuration, and uses DMX-512 (a specific RS-485 protocol) for command data. An additional RS-485 transceiver was included for a future hydraulic system monitoring project.

Aside from handling data, the GSE also provides various enable signals for the valve bank module electronics. Each channel's hydraulic vavle driver, as well as the Br-EFB (the PID controller for all 4 channels in each bank), has an indiviudal enable. There is also a port for a remote e-stop button which must be connected in order to enable anything in the valve bank box.

This project is still in progress. The front panel has just been delivered from Front Panel Express (Sep 14). The panel will be powder-coated, and then the electronics will be assembled onto the panel.