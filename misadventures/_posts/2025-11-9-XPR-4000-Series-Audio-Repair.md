---
layout: post
category: misadventures
title: Motorola XPR 4000 Series Audio Repair
---
![Motorola XPR 4550](/images/XPR4000_Series/XPR4550.jpg)

A somewhat common issue with these radios is losing all audio. If a unit’s built-in speaker doesn’t make a pop sound or power-on tone when powered on — and the codeplug checks out fine — the audio amplifier has likely failed.<!--more-->

Here is a block diagram of the audio path within the XPR 4000 series of mobiles, taken from the <a href="https://blog.magnumelectronics.com/wp-content/uploads/2015/07/xpr4000_service_manual_6880309t22-f.pdf" target="_blank">detailed service manual</a>.

<a href="https://aramd.net/images/XPR4000_Series/XPR_audio_BD.png"><img src="/images/XPR4000_Series/XPR_audio_BD.png" alt="XPR internal audio path block diagram"></a>

The culprit is U3500, the TDA1519C final audio amplifier IC. It seems that there’s some issue causing these amplifiers to fail at a non-negligible rate in these radios. Per the datasheet, these ICs have internal thermal protection, so it’s unlikely that the problem is simply poor thermal contact with the heatsink. Perhaps an edge-case turn-on transient causes some kind of violent instability? The radios I’m repairing were used to drive an intercom system, which shouldn’t present much of a load to the amplifier output.

Unfortunately, the TDA1519C is discontinued. Thankfully, there are still a handful of gray-market parts available from the usual suspects.

## Disassembly

First, remove the outer plastic cover/jacket. This is done by simply prying it to the sides.

<a href="https://aramd.net/images/XPR4000_Series/remove_outer_jacket.jpg"><img src="/images/XPR4000_Series/remove_outer_jacket.jpg" alt="Remove outer jacket"></a>

At this point, you should probably remove the control head before removing the lid and exposing the PCB. *Do as I say, not as I do* and all that. The control head must be pried off, and one or two ribbon cables disconnected from the main PCB depending on the options in a particular unit. Do not leave any ribbon cables connected to the main board, as we’ll be removing it from the enclosure.

Remove the seven fasteners with a T20 driver. Note that each screw has an o-ring that must be reinstalled between the body and the lid prior to reinsertion. Some units that have been serviced previously might not have these o-rings.

<a href="https://aramd.net/images/XPR4000_Series/enclosure_screws.jpg"><img src="/images/XPR4000_Series/enclosure_screws.jpg" alt="Lid with screws."></a>

Now remove the lid to expose the PCB.

<a href="https://aramd.net/images/XPR4000_Series/lid_removed.jpg"><img src="/images/XPR4000_Series/lid_removed.jpg" alt="Lid removed, first view of top of PCB"></a>

To remove the PCB:
* Remove the MAP accessory connector (black plastic housing with 0.1" pins on the rear of the unit) by pulling it out the back. The only thing retaining it is the friction of the contacts and gasket.
* Disconnect the internal GPS antenna cable.
* Remove the two retaining clips on the power and mini UHF connectors. These can be pulled off with pliers and a gentle side-to-side wiggle. **Be careful not to damage the PCB during this step!** It’s easy to slip and damage traces or components.

<a href="https://aramd.net/images/XPR4000_Series/clips_removed.jpg"><img src="/images/XPR4000_Series/clips_removed.jpg" alt="Clips and other such retention devices removed."></a>

Now the PCB can be tilted up and removed from the housing. Immediately upon lifting the board, you’ll likely notice the unmistakable smell of fried electronics if the audio amplifier has failed. Before even flipping over the PCB, you may see residue on the housing near the amplifier.

<a href="https://aramd.net/images/XPR4000_Series/three_unit_failure_residue.jpg"><img src="/images/XPR4000_Series/three_unit_failure_residue.jpg" alt="Residue from amplifier failure."></a>

Turning the PCB over, the audio amp is located on the left side of the board.

<a href="https://aramd.net/images/XPR4000_Series/PCB_bottom.jpg"><img src="/images/XPR4000_Series/PCB_bottom.jpg" alt="PCB bottom view."></a>

Inspecting multiple units, the audio amplifier seems to fail catastrophically and consistently in the same way.

<a href="https://aramd.net/images/XPR4000_Series/three_unit_failure_inspection.jpg"><img src="/images/XPR4000_Series/three_unit_failure_inspection.jpg" alt="Inspecting the audio amp for failure."></a>

## Examining the Circuit

It seems that the same pins are damaged across units.

<a href="https://aramd.net/images/XPR4000_Series/damaged_ICs.jpg"><img src="/images/XPR4000_Series/damaged_ICs.jpg" alt="Damaged audio amp ICs" style="max-height:600px"></a>

These correspond to the pins shown in the <a href="https://www.nxp.com/docs/en/data-sheet/TDA1519C.pdf" target="_blank">TDA1519C datasheet</a>.

<a href="https://aramd.net/images/XPR4000_Series/TDA1519C_pinout.png"><img src="/images/XPR4000_Series/TDA1519C_pinout.png" alt="Damaged audio amp IC pins" style="max-height:600px"></a>

The suggested implementation in the datasheet matches the circuit used in the XPR 4000 series, per the <a href="https://blog.magnumelectronics.com/wp-content/uploads/2015/07/xpr4000_service_manual_6880309t22-f.pdf" target="_blank">detailed service manual</a> sheet 124.

<a href="https://aramd.net/images/XPR4000_Series/TDA1519C_internal_BD.png"><img src="/images/XPR4000_Series/TDA1519C_internal_BD.png" alt="Audio amp datasheet application circuit"></a>

<a href="https://aramd.net/images/XPR4000_Series/schematic_snippet.png"><img src="/images/XPR4000_Series/schematic_snippet.png" alt="XPR 4000 series schematic snippet"></a>

## Repair

Rather than trying to desolder and remove the IC in one go, I suggest snipping the *remaining* leads with small wire cutters, then desoldering the individual pins. Done carefully, this stresses the PCB less than trying to desolder the entire chip at once.

Sometimes the leads are nice enough to vaporize themselves, so you don’t even have to cut them!
<a href="https://aramd.net/images/XPR4000_Series/OUCH.jpg"><img src="/images/XPR4000_Series/OUCH.jpg" alt="Very violent failure."></a>

After desoldering and wicking the remaining solder, inspect the pads for damage. In two of the three units I repaired, the pads were fine, but in the worst unit, the pin 7 “Vp” pad seemed to have sacrificed itself as a fuse.

<a href="https://aramd.net/images/XPR4000_Series/cleaned_pads.jpg"><img src="/images/XPR4000_Series/cleaned_pads.jpg" alt="Damaged solder pads"></a>

Install the new part. If you’re feeling like being extra thorough, you might also replace the thermal pad between the audio amp IC and the enclosure. The stock pad is 1mm thick, and about 12 x 20mm. Any generic 1mm pad can be cut to size and used in this application.

Be sure to clean the PCB and enclosure before reassembly. The nearby thermal pad/adhesive often has gunk embedded in it from the explosion in failed units — check yours carefully. We wouldn’t want a piece of FOD causing more issues.

<a href="https://aramd.net/images/XPR4000_Series/cleaned.jpg"><img src="/images/XPR4000_Series/cleaned.jpg" alt="Cleaned area of damage to enclosure"></a>

Reassemble in reverse order of disassembly.

## Resources

* TDA1519C Datasheet - <a href="https://www.nxp.com/docs/en/data-sheet/TDA1519C.pdf" target="_blank">NXP</a>
* Service Manual (UHF) - <a href="https://blog.magnumelectronics.com/wp-content/uploads/2015/07/xpr4000_service_manual_6880309t22-f.pdf" target="_blank">Magnum Electronics</a>
  * They also maintain an extensive modern Batwing <a href="https://blog.magnumelectronics.com/pdf-library-2/" target="_blank">document library</a> with many full service manuals.
* Video of technician performing this repair on an XPR 4550 - <a href="https://www.youtube.com/watch?v=6nWnsMUx3_E" target="_blank">Blue Mountain Radios on YouTube</a>
