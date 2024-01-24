---
layout: post
category: animation
title: San Diego Zoo Animation 2024
---
![Completed parade float going down the parade route](/images/San Diego Zoo 2024/float.jpg)

In late 2023, I was once again contracted by Artistic Entertainment Services (AES) to reconfigure the animatronic control system I designed and built with them last year for the new San Diego Zoo Wild Animal Park's 2024 Tournament of Roses entry. Like last year, this float features a cast of zoo residents animated to interact with riders on the float. I am thrilled that this float won the sweepstakes award for the most beautiful entry!<!--more-->

![Animation computer panel](/images/San Diego Zoo 2024/setup.jpg)

![Animation computer panel](/images/San Diego Zoo 2024/bench test.jpg)

![Animation computer panel](/images/San Diego Zoo 2024/main enclosure.jpg)

![Animation computer panel](/images/San Diego Zoo 2024/relays.jpg)

{% include youtubePlayer.html id="od3xIjQe9LI" %}

*Top photo of completed float courtesy of the San Diego Zoo Wildlife Alliance*

================

The two giraffes were essentially mechanically identical, using a large hydraulic cylinder for the neck lift, and two motors for head rotation and tongue actuation. These two giraffes were the only elements on the float which required closed loop control, so only 4 channels of closed loop motor control and 2 channels of hydraulic control were required. 


The main computer was based around Gilderfluke a show controller and two 4-axis PID controllers in a similar arrangement to the system I built for LCFTRA's animation system. I designed the panel shown above with 4 channels of DC brushless motor current controlled drive, and 2 channels of current controlled drive for proportional hydraulic valves. AES's skilled technical/electrical department assembled this beautiful panel (the photo doesn't show it 100% complete and tidied up) based on my drawings. For the operator interface with the system, I had AES cut out an aluminum panel for this controller which I assembled.

![Animation system controller](/images/San Diego Zoo 2024/controller.jpg)

It was quite nice to work with a company who builds hardware like this regularly. I was able to have their mechanical engineers and machinist rapidly design this panel and manufacture it! The engraving infill turned out really great.

![Animation system controller internal wiring](/images/San Diego Zoo 2024/controller wiring.jpg)

This controller was the main part of the system that I had to wire up, other than the "Gilderfluke Ground Support Equipment" or "G2SE" box which I made in parallel with this project as a tool for myself. The unit combines 8 channels of high resolutions sliders which appear as joystick inputs to the Gilderfluke PCMACS programming software, and it also contains ethernet, RS-232, and RS-485 adapters for interfacing with the animation system. It can be seen on the left side of the table during this late night programming session, and you can read more about it <a href="https://aramd.net/G2SE/">here</a>!

![Late night programming session with computer and support equipment on table with float in the background](/images/San Diego Zoo 2024/programming session.jpg)

Since the float was being worked on during regular working hours, I had to do most of the animation system setup and programming after hours. Tuning the PIDs for the feedback system was straight forward, however, but setting up the actual animations was time consuming given the numerous collision zones that the giraffes had. In the end, the proximity of the giraffes during certain portions of the animation show really added to the overall animation.



I'm really glad I had the opportunity to work with AES on this project. I think the results looked great... as did the Tournament of Roses. I'm quite proud that this float won the Tournament's Animation Award for most outstanding use of animation in the parade!

![Me in the back of the safari truck taking a selfie with the giraffes](/images/San Diego Zoo 2024/me and the boys.jpg)
