SET AMPY_PORT="COM3"

echo '### Erase flash ###'
esptool --chip esp32 --port %AMPY_PORT% erase_flash

echo '### Flash microPython ###'
esptool --chip esp32 --port %AMPY_PORT% write_flash -z 0x1000 ..\firmware\esp32-20180120-v1.9.3-240-ga275cb0f.bin

echo '### Remove boot.py ###'
ampy rm boot.py >/dev/null 2>&1  # TODO: Fix this command failing 

echo '### Make directories ###'
ampy --port %AMPY_PORT% --delay 1 mkdir configuration
ampy --port %AMPY_PORT% --delay 1 mkdir lib
ampy --port %AMPY_PORT% --delay 1 mkdir lib/aiko
ampy --port %AMPY_PORT% --delay 1 mkdir lib/umqtt

echo '### Copy configuration/*.py ###'
ampy --port %AMPY_PORT% --delay 1 put ..\configuration\led.py      configuration/led.py
ampy --port %AMPY_PORT% --delay 1 put ..\configuration\lolibot.py  configuration/lolibot.py
ampy --port %AMPY_PORT% --delay 1 put ..\configuration\mqtt.py     configuration/mqtt.py
ampy --port %AMPY_PORT% --delay 1 put ..\configuration\services.py configuration/services.py
ampy --port %AMPY_PORT% --delay 1 put ..\configuration\wifi.py     configuration/wifi.py

echo '### Copy lib/aiko/*.py ###'
ampy --port %AMPY_PORT% --delay 1 put ..\lib\aiko\led.py      lib/aiko/led.py
ampy --port %AMPY_PORT% --delay 1 put ..\lib\aiko\mqtt.py     lib/aiko/mqtt.py
ampy --port %AMPY_PORT% --delay 1 put ..\lib\aiko\services.py lib/aiko/services.py
ampy --port %AMPY_PORT% --delay 1 put ..\lib\aiko\wifi.py     lib/aiko/wifi.py

echo '### Copy lolibot.py ###'
ampy --port %AMPY_PORT% --delay 1 put ..\lib\lolibot.py lib/lolibot.py

echo '### Copy mpu9250.py ###'
ampy --port %AMPY_PORT% --delay 1 put ..\lib\mpu9250.py lib/mpu9250.py 

echo '### Copy lib/umqtt ###'
ampy --port %AMPY_PORT% --delay 1 put ..\lib\umqtt\simple.py lib/umqtt/simple.py
ampy --port %AMPY_PORT% --delay 1 put ..\lib\umqtt\robust.py lib/umqtt/robust.py

echo '### Copy boot.py ###'
ampy --port %AMPY_PORT% --delay 1 put ..\boot.py

echo '### Complete ###'