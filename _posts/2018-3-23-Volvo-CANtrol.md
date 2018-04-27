---
layout: post
title: Volvo/Whelen CANtrol
---
![alt text]({{site.baseurl}}/images/Volvo\ CANtrol/footwell.jpg)

Have you ever had a piece of equipment that really REALLY doesn't belong in your car, but you want to install it somehow? Well, I had this problem with my Whelen... electric airhorn.... I initially installed it above my leg in the footwell, since that's the only place I could fit the unit. Now, you're probably saying "won't you obliterate your leg in an accident?", and the answer to that is yes, yes I will. So a solution is needed for remote mounting and control!

I had looked into remote mounting for the unit before, but I couldn't come up with a clean remote control interface. Recently, one of my friends was talking about accessing a car's CAN bus for a project he was working on, and I realized I could probably use some of the car's buttons to control the Whelen unit over the car's CAN bus.

I'm not one to use cruise control, so I decided to use the cruise control buttons on the steering wheel for this project. I ended up using the following buttons:

-Cruise restart --> Whelen HORN button
-Cruise hold --> Whelen MAN button
-Speed + --> Increment selected mode up
-Speed - --> Increment selected mode down

So that the cruise function is still usable, when cruise control is activated, the speed adjustment buttons will not cause any changes to the Whelen unit's selected operating mode.

After looking through the Volvo S60/S80 2003 wiring diagram, I found a convenient CAN bus access point under the driver's seat. Volvo's color code for the CAN bus is White = CAN H, Green = CAN L. I tapped into the bus entering the connector for the power seat module with positaps, and began looking for packets corresponding to buttons on the steering wheel.
