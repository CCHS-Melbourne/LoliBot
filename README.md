# LoliBot - The ESP32 Based Soccer bot.

Quick links ...

  * [Hardware assembly](http://www.openhardwareconf.org/wiki/LoliBot-Assembly)
  * [Software installation and usage](software)

Welcome to the 2018 linux.conf.au Open Hardware Project.  You can see information about this and other MiniConfs at <http://www.openhardwareconf.org/wiki/Main_Page>.

If you're attending the assembly workshop at Linux.conf.au 2018, the place to start is <http://www.openhardwareconf.org/wiki/LoliBot>

This year's project is called the Lolibot, and is a simple robot is designed to chase and kick a Ping Pong ball around.

It features a Lolin32-lite ESP32 based chip as it's primary microprocessor and includes a MPU6050 6 axis accelerometer.

In order to reduce complexity and to be a bit more flexible with our design this years project is a platform with discrete components.
Those of you who are looking forward to the smell of melting solder won't be disappointed though, there are many headers, LEDS and switches to keep you busy.

## Hardware

### Screen Shots

![LoliBot Render](LoliBot-Render-Top.png?raw=true "Render")

### Assembly

Assembly instructions for the kit are at <http://www.openhardwareconf.org/wiki/LoliBot-Assembly>

### Hardware Links

* [WEMOS LOLIN32](https://wiki.wemos.cc/products:lolin32:lolin32)
* [mpu-6050](https://www.invensense.com/products/motion-tracking/6-axis/mpu-6050/) TBD lots of options
* [Wheels](https://www.aliexpress.com/item/TT-Motor-130motor-with-the-wheel-Smart-Car-Robot-Gear-Motor-for-Arduino-DC3V-6V-DC/32829319427.html) one of many like this..

### datasheets

* [L9110 Motor control driver chip](datasheets/datasheet-l9110.pdf)

## Software

All the usual ESP32 development options apply to the LoliBot ...

 * microPython scripts
 * Arduino IDE sketches
 * Native ESP-IDF FreeRTOS firmware

We've chosen to focus on using microPython to provide a simple, yet
capable entry point for newcomers to robotics and embedded computers.

The [software sub-directory has instructions](software)
 on installing and developing software for the LoliBot.

## LICENSE

Licensed under the TAPR Open Hardware License (<http://www.tapr.org/OHL>). The "license" sub-folder also contains a copy of this license in plain text format.

Copyright John Spencer, Angus Gratton, Andy Gelme, Jon Oxer, Mark Wolfe 2017
