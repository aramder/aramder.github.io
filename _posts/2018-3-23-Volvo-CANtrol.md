---
layout: post
title: Volvo/Whelen CANtrol
---
![Looking down into my footwell with equipment uncomfortably close to my leg](/images/Volvo CANtrol/footwell.jpg)

Have you ever had a piece of equipment that really REALLY doesn't belong in your car, but you want to install it somehow? Well, I had this problem with my Whelen... electric airhorn....<!--more--> I initially installed it above my leg in the footwell, since that's the only place I could fit the unit. Now, you're probably saying "won't you obliterate your leg in an accident?", and the answer to that is yes, yes I will. So a solution is needed for remote mounting and control!

I had looked into remote mounting for the unit before, but I couldn't come up with a clean remote control interface. Recently, one of my friends was talking about accessing a car's CAN bus for a project he was working on, and I realized I could probably use some of the car's buttons to control the Whelen unit over the car's CAN bus.

I'm not one to use cruise control, so I decided to use the cruise control buttons on the steering wheel for this project. I ended up using the following buttons:


* Cruise restart --> Whelen HORN button
* Cruise hold --> Whelen MAN button
* Speed + --> Increment selected mode up
* Speed - --> Increment selected mode down

So that the cruise function is still usable, when cruise control is activated, the speed adjustment buttons will not cause any changes to the Whelen unit's selected operating mode.

![A screenshot from Volvo's wiring diagram showing access to the CAN bus](/images/Volvo CANtrol/powered seat CAN.png)

After looking through the Volvo S60/S80 2003 wiring diagram, I found a convenient CAN bus access point under the driver's seat. Volvo's color code for the CAN bus is White = CAN H, Green = CAN L. I tapped into the bus entering the connector for the power seat module with positaps, and began looking for packets corresponding to buttons on the steering wheel.

![A spreadsheet of some CAN mesages](/images/Volvo CANtrol/packet table.png)

After messing around for quite a while, I found the ID for CAN packets containing information about the steering wheel's buttons. There are a number of other outputs for combinations of buttons, but this data is more than enough for what I want to do.

It was only after wasting a lot of time finding and decoding these messages that I saw a post on Hacking Volvo that mentioned CAN messages relating to steering wheel controls.... Oh well. There's a lot more about decoding and replicating packet data on the blog. Check it out at the <a href="http://hackingvolvo.blogspot.com" target="_blank"> Hacking Volvo Blog</a>.

Olaf's 2002 S80's CAN packets seem to have the same data formatting as my 2003 S60, but CAN IDs are slightly different (comparing what he's posted on his blog and what I've found experimentally). That being said, knowing what data relating to the steering wheel looks like should at least help anyone trying to sniff the CAN bus on their car.

![Testing electronics on a breadboard](/images/Volvo CANtrol/breadboard.jpg)

Prototype controller (right half of breadboard) used for decoding CAN packets and testing control functions.

![Electronics assembled on a breadboard](/images/Volvo CANtrol/perfboard.jpg)

Controller spread out between two perf-board assemblies. The left board has the Arduino Pro Mini, a MCP2515 CAN module, and a voltage regulator. The right board as a few transistors and a 74LS138 (binary decoder) for controlling the Whelen unit.

![Showing the internal wiring within the Whelen unit](/images/Volvo CANtrol/internal wiring.jpg)

A ribbon cable will connect the siren to the controller unit. Signals such as the MAN, HORN, and SHDN lines will go to the three transistors to simulate contact closures. Seven lines from the rotary mode select switch will go to the 74LS138 to select the unit's operating mode. The rotary switch usually pulls one of the seven lines low (all lines have a pullup to 5v), which goes to a microcontroller. Since the 74LS138 has active low outputs, Y0 through Y6 can be directly connected to the seven mode select lines.


![Testing the Whelen unit and controller on a testbench](/images/Volvo CANtrol/testing.jpg)

The ribbon cable installed, testing with the controller.


![A closeup of the two controller boards](/images/Volvo CANtrol/testing 1.jpg)

A closeup of the two controller boards.

![Whelen unit and controller sitting in the back seat of my car](/images/Volvo CANtrol/install.jpg)

Testing the buttons/CAN/controller/Whelen interface in my car before installing everything.

![A clseup of the controller in a small plastic enclosure](/images/Volvo CANtrol/install 1.jpg)

The controller installed in a small plastic box.

![The controller tapped to the side of the Whelen unit, ready for install](/images/Volvo CANtrol/install 2.jpg)

The controller tapped to the side of the Whelen unit, ready for install.

![The whelen unit installed under the driver's seat](/images/Volvo CANtrol/under seat.jpg)

The Whelen unit sitting under the driver's seat. You'll notice a factory wire harness which would connect to powered seats. At the bottom of the photo (half obscured by the slide release handle) is the connector I used to tap into the car's CAN bus.

![The whelen unit under the driver's seat with a handheld microphone on the side of the footwell](/images/Volvo CANtrol/under seat 1.jpg)

The installed Whelen and CANtrol (this is what Whelen calls their CAN interfacing stuff) units with the PA (Public Address) hand mic hanging from a holder in the driver's footwell. The seat has been lifted and moved back for this photo; when the seat's in the position I drive in, the mic sits approximately under my knee where it doesn't bother me at all.
