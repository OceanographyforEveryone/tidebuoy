# Bristlemouth Tide Buoy
Documentation and support for a bristlemouth-integrated tide gauge buoy, using parts and software borrowed from the OpenCTD. 

Read about the  project, and the work of the St. Michaels Climate Change/Sea level Rise Commission, here: [St. Michaels Floodwatch](https://www.stmichaelsfloodwatch.com/)

## Hardware

The Tide Buoy uses an [Adafruit Feather RP2040](https://www.adafruit.com/product/4884) connected to the [Bristlemouth DevKit](https://www.bristlemouth.org/pioneer) via an [OpenCTD carrier board](https://oceanographyforeveryone.bigcartel.com/product/openctd-rev-7c-custom-carrier-board). The pressure and temperature sensor is a MS5803-14BA on a DIY circuit board (but a commercial breakout board is available from [Sparkfun](https://www.sparkfun.com/sparkfun-pressure-sensor-breakout-ms5803-14ba.html). 

The pressure sensor is potted in a 3D printed housing that is screwed, along with a spacer, to the bottom of the DevKit. The 3D Parts File can be found here: [3D Printed Parts](https://github.com/OceanographyforEveryone/tidebuoy/tree/main/3D%20Printed%20Parts). A [Blue Robotics WetLink Penetrator](https://bluerobotics.com/store/cables-connectors/penetrators/wlp-vp/) is used to routh the wires through the base of the DevKit housing. 

## Firmware

To prepare you Spotter Buoy, reference the Bristlemouth [Development Kit User Guides](https://bristlemouth.notion.site/Development-Kit-User-Guides-e9ca1b3c5a1c41c890d0105f2eb7c4b8) and, especially, [Bristlemouth Dev Kit Guide: Serial Client for CircuitPython](https://bristlemouth.notion.site/Bristlemouth-Dev-Kit-Guide-Serial-Client-for-CircuitPython-8a04e3bd59604b419228ac9abaf18c3e). A circuit python library and sample code for the pressure sensor is provided here: [MS5803-14BA](https://github.com/OceanographyforEveryone/tidebuoy/tree/main/Firmware/MS5803-14BA) and the python script to run on the tide buoy, which is currently set to sample once every 15 minutes, is available here: [code.py](https://github.com/OceanographyforEveryone/tidebuoy/blob/main/Firmware/code.py). 

## Visualization

Real-time date from the tide buoy can be charted over a 24-hour cycle using this html script: [chart](https://oceanographyforeveryone.github.io/tidebuoy/chart) while the last 12 sensor readings can be recalled using this html script: [readings](https://oceanographyforeveryone.github.io/tidebuoy/readings.html). Barometric pressure is normalized against the most recent reading from the [NOAA Annapolis weather station](https://tidesandcurrents.noaa.gov/stationhome.html?id=8575512).  

## Correction factors for Tide Buoy currently deployed in Honeymoon Lagoon

Correction factor for MLLW: 1.8

Correction factor for MSL: 2.3
