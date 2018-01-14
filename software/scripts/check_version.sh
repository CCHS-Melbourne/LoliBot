#!/bin/sh

ampy get boot.py | grep version:

ampy get lib/lolibot.py | grep version:

ampy get lib/aiko/led.py      | grep version:
ampy get lib/aiko/mqtt.py     | grep version:
ampy get lib/aiko/services.py | grep version:
ampy get lib/aiko/wifi.py     | grep version:

ampy get configuration/led.py      | grep version:
ampy get configuration/lolibot.py  | grep version:
ampy get configuration/mqtt.py     | grep version:
ampy get configuration/services.py | grep version:
ampy get configuration/wifi.py     | grep version:
