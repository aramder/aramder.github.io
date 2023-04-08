---
layout: post
category: projects
title: San Diego Zoo Animation 2023
---
![Completed parade float ready to go down the route](/images/projects/San Diego Zoo/parade morning.jpg)

In late 2022, I was contracted by Artistic Entertainment Services (AES) to design and program an animatronic control system for the San Diego Zoo Wild Animal Park's 2023 Tournament of Roses Entry. This rapid turnaround project leveraged compact electrical and hydraulic driven mechanisms to animate a pair of giraffes which park guests are interacting with from the back of a safari truck. <!--more-->

The two giraffes were essentially mechanically identical, using a large hydraulic cylinder for the neck lift, and two motors for head rotation and tongue actuation. These two giraffes were the only elements on the float which required closed loop control, so only 4 channels of closed loop motor control and 2 channels of hydraulic control were required. 

![Animation computer panel](/images/projects/San Diego Zoo/computer panel.jpg)

The main computer was based around Gilderfluke a show controller and two 4-axis PID controllers in a similar arrangement to the system I built for LCFTRA's animation system. I designed the panel shown above with 4 channels of DC brushless motor current controlled drive, and 2 channels of current controlled drive for proportional hydraulic valves. AES's skilled technical/electrical department assembled this beautiful panel (the photo doesn't show it 100% complete and tidied up) based on my drawings. For the operator interface with the system, I had AES cut out an aluminum panel for this controller which I assembled.

![Animation system controller](/images/projects/San Diego Zoo/controller.jpg)

It was quite nice to work with a company who builds hardware like this regularly. I was able to have their mechanical engineers and machinist rapidly design this panel and manufacture it! The engraving infill turned out really great.

![Animation system controller internal wiring](/images/projects/San Diego Zoo/controller wiring.jpg)

This controller was the main part of the system that I had to wire up, other than the "G2SE" ground support equipment box which I made in parallel with this project. I'll probably make a separate post about it some other time.... It can be seen on the left side of the table during this late night programming session.

![Late night programming session with computer and support equipment on table with float in the background](/images/projects/San Diego Zoo/programming session.jpg)

Since the float was being worked on during regular working hours, I had to do most of the animation system setup and programming after hours. Tuning the PIDs for the feedback system was straight forward, however, but setting up the actual animations was time consuming given the numerous collision zones that the giraffes had. In the end, the proximity of the giraffes during certain portions of the animation show really added to the overall animation.

{% include youtubePlayer.html id="NDEyiNIk5Go" %}

I'm really glad I had the opportunity to work with AES on this project. I think the results looked great... as did the Tournament of Roses. I'm quite proud that this float won the Tournament's Animation Award for most outstanding use of animation in the parade!

![Me in the back of the safari truck taking a selfie with the giraffes](/images/projects/San Diego Zoo/me and the boys.jpg)
