#!/bin/sh

if [ -z "$AMPY_PORT" ]; then
  echo This script updates all MicroPython code to the
  echo Lolibot.
  echo
  echo Please provide the AMPY_PORT environment variable
  echo containing the device name of the lolin32.
  echo e.g. AMPY_PORT=/dev/ttyUSB0 "$0"
  exit 1
fi

echo '### Remove boot.py ###'
ampy rm boot.py >/dev/null 2>&1  # TODO: Fix this command failing

echo '### Make directories ###'
for d in configuration lib lib/aiko lib/umqtt; do
  if ampy ls $d 2>&1 | grep RuntimeErr > /dev/null; then
    ampy mkdir $d
  fi
done

echo '### Copy configuration/*.py ###'
ampy put configuration/led.py      configuration/led.py
ampy put configuration/lolibot.py  configuration/lolibot.py
ampy put configuration/mpu9250.py  configuration/mpu9250.py
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

echo '### Copy udp_control.py ###'
ampy put lib/udp_control.py lib/udp_control.py

echo '### Copy mpu9250.py ###'
ampy put lib/mpu9250.py lib/mpu9250.py

echo '### Copy lib/umqtt ###'
ampy put lib/umqtt/simple.py lib/umqtt/simple.py
ampy put lib/umqtt/robust.py lib/umqtt/robust.py

echo '### Copy boot.py ###'
ampy put boot.py

echo '### Complete ###'

# miniterm.py $AMPY_PORT 115200
