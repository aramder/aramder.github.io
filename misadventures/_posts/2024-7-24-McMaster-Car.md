---
layout: post
category: misadventures
title: The McMaster-Car - a 7.5" Gauge E-Bike Pedal Car
---
![The McMaster-Car pedal car locomotive on the track at LALS](/images/McMaster-Car/mcmaster-car_side.jpg)

About a year ago, I began volunteering at the <a href="https://lalsrm.org/" target="_blank">Los Angeles Live Steamers Railroad Museum</a>, and quickly felt the need to build myself a train to zip around the club's ~1.5 miles of track located in the picturesque northeast corner of Griffith Park. Rather than build a prototypical locomotive, I decided to make what's commonly referred to as a "pedal car" with some unique features.<!--more-->

Rather than make the whole frame out of raw stock which I would have to machine, bend, weld, etc. I went with a more modular approach using "80/20" 1.5" square extruded aluminum. Instead of completely relying on human pedal power, I decided to use a Bafang BBS02 750W mid-drive motor kit meant for e-bikes. This e-bike motor can both provide pedal assist, or completely power the locomotive. Between these two design decisions, I hoped to circumvent the typical complex machining required to build either a pedal car or small electric "speeder" locomotive. This propensity to COTS (commercial-off-the-shelf) parts led me to name this locomotive the McMaster-Car, after <a href="https://www.mcmaster.com/" target="_blank">McMaster-Carr</a>, a well established online marketplace for all sorts of industrial components.

Before we get too far, I was lucky enough to be testing this at LALS when Lisa of <a href="https://www.youtube.com/@LisaKEntertainment" target="_blank">Lisa K Entertainment</a> on youtube was visiting the club. She took the McMaster-Car on a spin around the track and released this great video (in addition to two more focused on LALS and the public train rides we conduct on Sundays)!

{% include youtubePlayer.html id="91HNBuuE_mU" %}

Let's start at the suspension. This is one of the components where machining was unavoidable, however, I was able to save quite a lot of time by using the <a href="http://caltech-mce-lab.wikidot.com/" target="_blank">Caltech Jim Hall design lab's</a> Flow Mach 2B waterjet to cut some components.

![Waterjetting steel suspension components at the Caltech design lab](/images/McMaster-Car/waterjetting_suspension.jpg)

After waterjetting the plates, the only operations needed were to machine the parallel flat surfaces and chamfer the posts which are used to align the springs. The bearing blocks, however, needed to be machined manually... mostly. While I machine most of this by hand, I was able to machine the bearing pockets using a Bridgeport mill outfitted with a ProtoTRAK conversational CNC controller.

![Machined suspension components with spring posts and bearing blocks](/images/McMaster-Car/suspension_components.jpg)

Thankfully, I was also able to use a lathe outfitted with a similar ProtoTRAK controller to machine the 4" (contact diameter) wheels per the <a href="http://ibls.org/mediawiki/index.php/IBLS_Wheel_Standard" target="_blank">International Brotherhood of Live Steamers</a> wheel specification. I also broached a keyway into the wheels for indexing them on the locomotive's two 1" axles.

![Four 4-inch train wheels machined to IBLS specification with keyways](/images/McMaster-Car/wheels.jpg)

With the suspension and wheels done, the frame can begin to take shape. Rather than buying most of the interconnecting plates for the extruded aluminum, I was able to simply waterjet them out of scrap aluminum material very easily using existing CAD drawings I found online.

![Basic frame constructed from 80/20 extruded aluminum with waterjet plates](/images/McMaster-Car/basic_frame.jpg)

The next challenge was to mount a brake of some kind. Since the axles are sprung and have some play in practically all dimensions, I needed to mount the brake somewhere in the powertrain between the axles and the motor. Conveniently, a friend had suggested using an internally geared hub between the motor and axles, and some of these hubs can conveniently accommodate a brake rotor! I decided to us a Shimano Nexus SG-3D55 3-speed hub. As shown below, the input sprocket from the e-bike motor is on the left, and the ANSI 40 chain output which connects to the front axle is on the right.

![Shimano Nexus 3-speed hub with brake rotor installed on the frame](/images/McMaster-Car/geared_hub.jpg)

In order to transfer the output torque of the hub to the output chain, I needed to fix a sprocket to the hub. I was able to machine out the center of a large flat sprocket using another conversational CNC mill, and then drill and tap holes which matched the holes in the hub's flange intended for bicycle wheel spokes.

For reference, the sprocket tooth counts are as follows. These sprockets are sized to prioritize torque output.
* Motor output: 44 (Bicycle single speed chain)
* Hub input: 16 (Bicycle single speed chain)
* Hub output: 24 (ANSI 40 chain)
* Axle input: 17 (ANSI 40 chain)
* Axle to axle link: 12 (ANSI 40 chain)

![Custom output sprocket machined to mount on the hub's spoke flange](/images/McMaster-Car/geared_hub_output_sprocket.jpg)

The motor was mounted upside-down from the typical bicycle configuration using a couple of waterjet plates and a piece of tube which were later TIG welded together. This mockup on a short piece of extrusion also has an "18W" (they're really 12W) off-roading spotlight which will serve as a headlight.

![Bafang BBS02 motor and headlight mounted on TIG-welded bracket](/images/McMaster-Car/motor_mount.jpg)

With the motor mount completed, the train is looking mostly complete. Note that I had to use aftermarket 140mm crank arms rather than the stock 152mm crank arms to accommodate for the ergonomics of the motor to seat positioning.

![Nearly complete locomotive with motor, frame, and shortened crank arms](/images/McMaster-Car/mostly_complete.jpg)

The Bafang BBS02 motor actually integrates the motor drive electronics into the motor assembly, simplifying wiring considerably. The motor takes 48V directly from the 15Ah 13S3P 21700 Li-ion battery pack, and a second 48V feed was wired to a small DC/DC converter is used to generate 12V accessories. The box on the end of the frame contains 12V fusing, switching, and distribution for things like the headlight, horn (a small motorcycle horn), phone charger, and FRED. A FRED is a Flashing Rear End Device which is often required for operating scale trains at night, so I implemented one directly on the locomotive using a cheap motorcycle brake light and a digital PWM generator module.

![Rear enclosure with 12V distribution and flashing FRED tail light](/images/McMaster-Car/FRED.jpg)

Some zip ties and a boat seat later, and the McMaster-Car is ready for a test run!

![Ready for a test run on the completed McMaster-Car](/images/McMaster-Car/me_on_the_mcmaster-car.jpg)

It's quite a blast to zoom around the LALS track. I hope to continue to make updates to the McMaster-Car as I have time. Some major updates include a coupler and an airbrake system for use with various riding cars, and minor updates include things like adding cup holders for a water bottle or radio, and making the handles a bit more ergonomic.

![Front view of the McMaster-Car on the LALS track](/images/McMaster-Car/mcmaster-car_front.jpg)

Here's almost 10 minutes of unedited footage of a loop around the LALS track if you're craving a soundtrack for rereading this post.

{% include youtubePlayer.html id="-Lr9_5z4Kt0" %}

---

## Appendix: Parts List

> Added June 10, 2026. I've received a number of requests for more information on the design, so here's a breakdown of the major components used in this build.

A few recommendations for anyone looking to build a rail bicycle like this:

- Use a Shimano geared hub with an internal brake. The full sized brake disc is NOT worth it. Even with both axles braking, the train doesn't have enough braking force to warrant the pain of making the disc work.
- Steel is definitely overkill for the suspension and bearing blocks. Aluminum should do just fine and be easier to fabricate.

### Downloads

DXF files for the waterjet-cut suspension and bracket components:

- [Suspension slide plate](https://aramd.net/images/McMaster-Car/Suspension%20slide%20plate.dxf)
- [Spring Plate](https://aramd.net/images/McMaster-Car/Spring%20Plate.dxf)
- [Coupler bracket](https://aramd.net/images/McMaster-Car/Coupler%20bracket.dxf)
- [Safety Chain Plate](https://aramd.net/images/McMaster-Car/Safety%20Chain%20Plate.dxf)

### Frame Extrusion

**1.5" ultralight extrusion** from Automation Direct ([link](https://www.automationdirect.com/adc/shopping/catalog/structural_frames_-z-_rails/t-slotted_rails/1515cul)):

- 3qty 32" for chassis and motor mount
- 3qty 7" for chassis

**1" ultralight extrusion** from Automation Direct ([link](https://www.automationdirect.com/adc/shopping/catalog/structural_frames_-z-_rails/t-slotted_rails/1010c)):

- 2qty 9" for grips/handles
- 2qty 6" for grip/handle extensions
- 2qty 6.5" for seat mount

### Misc Hardware

- 1.5" slot nuts ([link](https://www.automationdirect.com/adc/shopping/catalog/structural_frames_-z-_rails/nuts_for_t-slotted_rails/161123))
- 1" slot nuts ([link](https://www.automationdirect.com/adc/shopping/catalog/structural_frames_-z-_rails/nuts_for_t-slotted_rails/151037))
- Flanged screws ([link](https://www.automationdirect.com/adc/shopping/catalog/structural_frames_-z-_rails/fasteners_for_t-slotted_rails/151041)), used for everything except the gusseted 90deg bracket
- Button head screws ([link](https://www.automationdirect.com/adc/shopping/catalog/structural_frames_-z-_rails/fasteners_for_t-slotted_rails/151040)), for gusseted 90deg bracket
- 4qty gusseted 90deg bracket for handles ([link](https://www.automationdirect.com/adc/shopping/catalog/structural_frames_-z-_rails/brackets_for_t-slotted_rails/151063))

### Suspension and Powertrain

- Springs ([McMaster 9657K354](https://www.mcmaster.com/9657K354/))
- Shaft ([McMaster 1497K101](https://www.mcmaster.com/1497K101/)). I ended up getting this 2ft shaft and cutting it into two 12" pieces.
- Shimano gear hub from [AliExpress](https://www.aliexpress.us/item/3256804859882701.html?spm=a2g0o.order_list.order_list_main.24.30521802wuDpop&gatewayAdapt=glo2usa)
- 160mm Shimano brake disc from [AliExpress](https://www.aliexpress.us/item/3256805479913835.html?spm=a2g0o.order_list.order_list_main.14.30521802wuDpop&gatewayAdapt=glo2usa)
- Shimano hydraulic brake kit from [AliExpress](https://www.aliexpress.us/item/3256805225676100.html?spm=a2g0o.order_list.order_list_main.41.30521802wuDpop&gatewayAdapt=glo2usa)
- Bafang shift sensor from [AliExpress](https://www.aliexpress.us/item/2255800663516901.html?spm=a2g0o.order_list.order_list_main.46.30521802wuDpop&gatewayAdapt=glo2usa)
- Bafang ebike Conversion Kit BBS02B 48V 750W. Unfortunately the listing I bought this from ended, but you can find it elsewhere on AliExpress.
- For the battery, I purchased a kit and assembled the battery pack myself. Presumably you can find the ebike motor and a ready-made battery from somewhere online.
- 140mm crank arms from [Amazon](https://www.amazon.com/gp/product/B0CM8Q14CM/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1). The standard length crank arms that come in the ebike kit are too long for a recumbent seating position.
- Motor mount tube: 1.5" OD x 0.083" wall x 1.334" ID aluminum round tube 6061-T6 from [Online Metals](https://www.onlinemetals.com/en/buy/aluminum/1-5-od-x-0-083-wall-x-1-334-id-aluminum-round-tube-6061-t6-drawn/pid/4361). I do not have the CAD for the bracket used for this tube.
- 12 tooth sprocket for #40 roller chain, 1" bore (40B12) from [The Big Bearing Store](https://www.thebigbearingstore.com/12-tooth-sprocket-for-40-roller-chain/)
- 24 tooth A plate sprocket for #40 roller chain (40A24) from [The Big Bearing Store](https://www.thebigbearingstore.com/24-tooth-a-plate-sprocket-for-40-roller-chain/)
- 17 tooth sprocket for #40 roller chain, 1" bore (40B17) from [The Big Bearing Store](https://www.thebigbearingstore.com/17-tooth-sprocket-for-40-roller-chain/)
- #40 roller chain, 10ft sections (40-1R) from [The Big Bearing Store](https://www.thebigbearingstore.com/40-roller-chain/)
- Shimano single speed chain. I purchased this in person from a bike shop.
- Bearings: fairly standard 1" sealed bearings. I bought these in person and don't recall the exact model.
- Several 1" shaft collars. I can't find the exact listing.

### Other

- Chair Wise 8WD734PLS-660 Low Back Boat Seat, Grey/Navy. Unfortunately the listing I bought this from ended, but you can find it online easily.
- 4 channel 12V relay board from [AliExpress](https://www.aliexpress.us/item/3256805663897937.html?spm=a2g0o.order_list.order_list_main.87.30521802wuDpop&gatewayAdapt=glo2usa)
- Timer module for flashing the FRED from [AliExpress](https://www.aliexpress.us/item/2251832828515637.html?spm=a2g0o.order_list.order_list_main.82.30521802wuDpop&gatewayAdapt=glo2usa)
- 48V to 12V 10A DC/DC converter from [AliExpress](https://www.aliexpress.us/item/3256805289139647.html?spm=a2g0o.order_list.order_list_main.150.30521802wuDpop&gatewayAdapt=glo2usa)
- 12V 6 circuit fuse block with ground from [Amazon](https://www.aliexpress.us/item/3256805289139647.html?spm=a2g0o.order_list.order_list_main.150.30521802wuDpop&gatewayAdapt=glo2usa)
- Headlight from [Amazon](https://www.amazon.com/gp/product/B01HTXANFC/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) (4 pack)
- Scooter taillight for FRED from [AliExpress](https://www.aliexpress.us/item/3256805675629576.html?spm=a2g0o.order_list.order_list_main.154.30521802wuDpop&gatewayAdapt=glo2usa)
- Enclosure for electronics from [Amazon](https://www.amazon.com/gp/product/B0BP7D59JK/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1), 8.7"x6.7"x4.3" option
