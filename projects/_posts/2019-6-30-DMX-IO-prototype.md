---
layout: post
category: projects
title: DMX Development Board
---
![The DMX development board - a printed circuit board assembly](/images/projects/DMX IO Prototype/DMX development board.jpg)

For a number of projects I'd like to work on in the future, I needed a development board of sorts for testing both hardware and software. <!--more-->

At the core of this development board is an Atmega328PB. This seems to be a rather interesting chip. It looks like after Microchip acquired Atmel, they looked at the Atmega328P (popularized by Arduino) and saw potential in improving this chip that already had a substancial foothold in the hobby market. So they added additional USART, I2C, and SPI peripherals, two timers, a peripheral touch controller, and more IO. Not only did they add all of these peripherals, but they also released the chip for about $0.50-0.60 **less** than the 328P. Rather interesting.

Connected to the Atmega328PB is a RS-485 transceiver for a DMX interface, PCA9685 (I2C 16-channel 12-bit PWM generator), 2 relays, and 4 MOSFETs (via the PCA9685).

*This is currently a work in progress. I have not had much time since the start of the semester to do much other than test basic functionality.*