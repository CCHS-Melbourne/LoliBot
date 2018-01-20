#!/bin/sh

echo '### Erase flash ###'
esptool.py --chip esp32 --port $AMPY_PORT erase_flash

echo '### Flash microPython ###'
esptool.py --chip esp32 --port $AMPY_PORT write_flash -z 0x1000 firmware/esp32-20180120-v1.9.3-240-ga275cb0f.bin

echo '### Remove boot.py ###'
ampy rm boot.py >/dev/null 2>&1  # TODO: Fix this command failing 

echo '### Make directories ###'
ampy mkdir configuration
ampy mkdir lib
ampy mkdir lib/aiko
ampy mkdir lib/umqtt

echo '### Copy configuration/*.py ###'
ampy put configuration/led.py      configuration/led.py
ampy put configuration/lolibot.py  configuration/lolibot.py
ampy put configuration/mqtt.py     configuration/mqtt.py
ampy put configuration/services.py configuration/services.py
ampy put configuration/wifi.py     configuration/wifi.py

echo '### Copy lib/aiko/*.py ###'
ampy put lib/aiko/led.py      lib/aiko/led.py
ampy put lib/aiko/mqtt.py     lib/aiko/mqtt.py
ampy put lib/aiko/services.py lib/aiko/services.py
ampy put lib/aiko/wifi.py     lib/aiko/wifi.py

echo '### Copy lolibot.py ###'
ampy put lib/lolibot.py lib/lolibot.py

echo '### Copy mpu9250.py ###'
ampy put lib/mpu9250.py lib/mpu9250.py 

echo '### Copy lib/umqtt ###'
ampy put lib/umqtt/simple.py lib/umqtt/simple.py
ampy put lib/umqtt/robust.py lib/umqtt/robust.py

echo '### Copy boot.py ###'
ampy put boot.py

echo '### Complete ###'

# miniterm.py $AMPY_PORT 115200
