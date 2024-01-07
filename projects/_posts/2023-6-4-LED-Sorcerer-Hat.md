---
layout: post
category: projects
title: LED Sorcerer Hat
---
![Illuminated sorcerer hat in a dark room](/images/LED Sorcerer Hat/hat in dark.jpg)

The basic LEDs that come in the Mickey sorcerer hat that Disney sells are rather pathetic. *We can rebuild him. We have the technology.* <!--more-->

This is a project I have been wanting to do for a while, but the prospect of writing all of the control software for the LEDs and making some kind of user interface kept me from getting started. Recently, a colleague pointed me to <a href="https://kno.wled.ge/">WLED</a>, an open source project that provides firmware for ESP8266/ESP32 devices and an accompanying app for configuring and operating the controller. The flexibility of the WLED controller is really allowing for really easy grouping of LED addresses and complex animations!

I built this very simple controller board using an ESP8266 (ESP01 format), which has some bulk capacitance for the LED supply, a 3.3V linear supply, and a simple single MOSFET voltage level converter for the LED data signal. I am simply using a USB battery bank to provide 5V to the controller via a long cable which lets me keep the battery bank in my pocket.

![Controller and LEDs](/images/LED Sorcerer Hat/ESP01 controller.jpg)

I used some generic wire wrap perforated FR2 board material as a backing to create clusters of five LEDs into stars. For the moon, I was able to kink the LED tape between LEDs to create the curve shape. For the wide part of the moon, I added a second piece of LED tape whose input data line I tapped off from a nearby LED on the main LED data path through the moon. For most of the wiring, I used some generic three-wire servo wire which helped to keep things neat.

![LEDs arranged in moon and star shapes](/images/LED Sorcerer Hat/moon and stars.jpg)

Installing the LEDs was a bit more of a pain than I expected. The way that the original LEDs were installed, there were large pieces of opaque fabric which covered most of the area of the stars and moon. This material had to be carefully cut out to fully expose the thin metallic fabric to the inside of the hat so that the light from the LEDs could effectively shine through.

In addition to the stars and moon, I put three long pieces of LED tape on back side of the hat's cone facing forwards to provide blue background illumination. The light is able to bounce around the cone and illuminate the hat fairly well.

![LEDs installed inside the hat](/images/LED Sorcerer Hat/LEDs installed.jpg)

Here I am looking far too excited after showing Mickey and Minnie my hat!

![Me wearing the illuminated hat](/images/LED Sorcerer Hat/if you know you know.jpg)
