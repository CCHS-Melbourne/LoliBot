#!/bin/sh

if [ -z "$AMPY_PORT" ]; then
  echo This script re-flashes the firmware and copies
  echo all MicroPython scripts to the board.
  echo
  echo Please provide the AMPY_PORT environment variable
  echo containing the device name of the lolin32.
  echo e.g. AMPY_PORT=/dev/ttyUSB0 "$0"
  exit 1
fi

D="`dirname $0`"

echo '### Erase flash ###'
esptool.py --chip esp32 --port $AMPY_PORT erase_flash

echo '### Flash microPython ###'
esptool.py --chip esp32 --port $AMPY_PORT write_flash -z 0x1000 firmware/esp32-20180120-v1.9.3-240-ga275cb0f.bin

"$D"/copy_micropython_scripts.sh
