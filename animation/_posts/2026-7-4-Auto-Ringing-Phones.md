---
layout: post
category: animation
title: "Ring and Play: Automated Themed Phones"
---
<div style="max-width: 70%; margin: 0 auto;">

![one_enclosure_one_phone](/images/Auto-Ringing_Phones/one_enclosure_one_phone.jpg)

</div>

I recently worked on a telephone installation for a themed venue that wanted a set of telephones for guests to interact with. The two phones sit inside and outside the venue, and ring occasionally to invite guests to pick up the handset. When someone answers, an in-character recording plays that matches the location and event.<!--more-->

To accomplish this, I used a telephone line simulator that handles phone power and generates ringdown voltage for the field handset, a basic timer module, a custom perfboard assembly with an audio transformer for injecting audio into the phone line, and a Gilderfluke Sd-25 MP3 player for playback.

<div style="max-width: 70%; margin: 0 auto;">

![panel](/images/Auto-Ringing_Phones/panel.jpg)

</div>

The panel is installed in a waterproof enclosure with just the two RJ12s for each unit's phone line and a 120VAC input cord.

![enlcosure](/images/Auto-Ringing_Phones/enlcosure.jpg)

The backstage connector is for debugging. It uses the same telephone line that the unit picks up to play the recorded audio for the guest on the handset.

The two units function independently, with different audio recordings for the inside and outside telephones. The auto-ring timer was set for a 10-minute countdown, so it would ring automatically every 10 minutes and reset whenever a guest picked up the phone.

![enclosure_connectors](/images/Auto-Ringing_Phones/enclosure_connectors.jpg)

Here are the two finished boxes, each paired with a test phone. For the actual installation, the client used period telephones connected directly to the system's analog Plain Old Telephone Service output.

![two_enclosures_two_phones](/images/Auto-Ringing_Phones/two_enclosures_two_phones.jpg)
