# Bristlemouth Tide Buoy
Documentation and support for a bristlemouth-integrated tide gauge buoy, using parts and software borrowed from the OpenCTD. 

Read about the full project, and the work of the St. MIchaels Climate Change/Sea level Rise Commission, here: [St. Michaels Floodwatch](https://www.stmichaelsfloodwatch.com/)

## Hardware

The Tide Buoy uses an [Adafruit Feather RP2040](https://www.adafruit.com/product/4884) connected to the [Bristlemouth DevKit](https://www.bristlemouth.org/pioneer) via an [OpenCTD carrier board](https://oceanographyforeveryone.bigcartel.com/product/openctd-rev-7c-custom-carrier-board). The pressure and temperature sensor is a MS5803-14BA on a DIY circuit board (but a commercial breakout board is available from [Sparkfun](https://www.sparkfun.com/sparkfun-pressure-sensor-breakout-ms5803-14ba.html). 

The pressure sensor is potted in a 3D printed housing that is screwed, along with a spacer, to the bottom of the DevKit. A Blue Robotics WetLink Penetrator is used to routh the wires through the base of the DevKit housing. 

## Firmware

To prepare you Spotter Bouy 

## Visualization

Real-time date from the tide buoy can be charted over a 24-hour cycle using this html script: [chart](https://oceanographyforeveryone.github.io/tidebuoy/chart) while the last 12 sensor readings can be recalled using this html script: [readings](https://oceanographyforeveryone.github.io/tidebuoy/readings.html). Barometric pressure is normalized against the most recent reading from the [NOAA Annapolis weather station](https://tidesandcurrents.noaa.gov/stationhome.html?id=8575512).  

## Correction factors for Tide Buoy currently deployed in Honeymoon Lagoon

Correction factor for MLLW: 1.8

Correction factor for MSL: 2.3
