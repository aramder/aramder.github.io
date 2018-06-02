---
layout: post
category: lcftra
title: DTMF Controller
---
<img class="shrunk" src="/images/lcftra/DTMF controller/intercom box internal.jpg" alt="Our intercom and radio box mounted on the float">

Our float is equiped with a custom built intercom and radio system to allow the float's crew to communicate both within the float, and with external crew. Since the intercom box is mounted in the middle of the float where it's not easily accessible, we needed some way to be able to remotely interface with the radio.<!--more--> The solution I came up with was a small perfboard assembly that used a microcontroller to decode DTMF tones received by the float's radio to change the radio's operating channel or toggle a set of relays.

Controlling the float's radio via DTMF allows us to easily change the radio's operating channel from any radio. By using the autopatch automatic dialing function built into some of our radios we can quickly send the passsword and command tones very quickly

A few people on the float operating crew have handheld radios with an autopatch dialing feature (designed for use in rather old systems allowing radio users to place phone calls over the radio via specialized repeaters or base stations) to quickly send a series of DTMF tones to the float's radio to change channels. This feature lets us send the DTMF password and command tones very quickly, and only requires a 

![3D mockup of a PCBA](/images/lcftra/DTMF controller/DTMF controller 3D front.png)
