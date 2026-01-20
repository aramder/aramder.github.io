---
layout: post
category: animation
title: San Diego Zoo Animation 2024
---
![San Diego Zoo sweepstakes-winning float with Karen the orangutan and Rex the lion](/images/San Diego Zoo 2024/float.jpg)

In late 2023, I was once again contracted by Artistic Entertainment Services (AES) to reconfigure the animatronic control system I designed and built with them for the 2023 parade for reuse on the San Diego Zoo Wild Animal Park's 2024 Tournament of Roses entry. Like last year, this float features a cast of zoo residents animated to interact with riders on the float. I am thrilled that this float won the sweepstakes award for the most beautiful entry!<!--more-->

![Animation system components laid out on workbench during setup](/images/San Diego Zoo 2024/setup.jpg)

The main box of the animation computer was relatively unchanged. The original Gilderfluke Sd-50/8 show controller and two Br-EFB quad PID controllers are still at the heart of this show. We only used one of the original four 48V motor drivers this year, in favor of external 220V VFDs for the remaining three axis of closed loop actuation. The PID controlled axes were...

* Karen the orangutan's head (48V brushed motor)
* Karen the orangutan's arm (220V 3-phase motor)
* Karen the orangutan's waist (220V 3-phase motor)
* Rex the lion's head/neck lift (220V 3-phase motor)

![DMX relay box for controlling the flamingo motors](/images/San Diego Zoo 2024/relays.jpg)

In addition to the addition of three VFSs, we also had to build a DMX relay box for powering motors for the eight flamingos on the float. The flamingo mechanisms were simple 12V brushed motors which drove a cam mechanism to rotate the necks. Rather than running the motors continuously, I pulsed them on and off to achieve the twitching motion displayed by flamingos in packs. There were also two relays added to the main controller to trigger some other animation features.

* 8x DMX controlled relays for switching 12V to flamingos
* 1x Sd-50/8 show controller driven relay for 120VAC to the butterfly's flapping wings
* 1x Sd-50/8 controlled relay for triggering the lion's roar audio

![Complete animation system during bench testing before float installation](/images/San Diego Zoo 2024/bench test.jpg)

Before installing the various boxes on the float, we set everything up on a bench for a quick test. Here you can see the whole system (from left to right): the VFDs on the far left of the desk before installation in their enclosure, the relay box sitting on the main box, the main controller, the switch box (used to enable axis and provide show control inputs), my <a href="https://aramd.net/G2SE/">custom animation GSE</a>, and laptop.

Not seen in this configuration is the Gilderfluke Sd-10 MP3 player which was triggered by the show controller in synchronization with the show. Each time the Rex the lion would roar, Karen the orangutan would pull the butterfly close to her chest to protect it, and the flamingos go berserk for a brief moment before returning to their typical animation loop.

![Main animation enclosure installed and ready for the parade](/images/San Diego Zoo 2024/main enclosure.jpg)

Here's a photo of the main box installed in the float and ready to go down the parade route!

{% include youtubePlayer.html id="od3xIjQe9LI" %}

*First photo of completed float courtesy of the San Diego Zoo Wildlife Alliance*
