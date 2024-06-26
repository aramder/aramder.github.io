---
layout: post
category: misadventures
title: DMX Development Board
---
![The DMX development board - a printed circuit board assembly](/images/DMX IO Prototype/DMX development board.jpg)

For a number of projects I'd like to work on in the future, I needed a development board of sorts for testing both hardware and software. <!--more-->

At the core of this development board is an Atmega328PB. This seems to be a rather interesting chip. It looks like after Microchip acquired Atmel, they looked at the Atmega328P (popularized by Arduino) and saw potential in improving this chip that already had a substancial foothold in the hobby market. So they added additional USART, I2C, and SPI peripherals, two timers, a peripheral touch controller, and more IO. Not only did they add all of these peripherals, but they also released the chip for about $0.50-0.60 **less** than the 328P. Rather interesting.

Connected to the Atmega328PB is a RS-485 transceiver for a DMX interface, PCA9685 (I2C 16-channel 12-bit PWM generator), 2 relays, and 4 MOSFETs (via the PCA9685 and a gate driver).

The scope of my senior project shifted after some testing with this board and reevaluating our team's goals. Details on that project can be found <a href="https://aramd.net/ELC-summary/">here</a>.
