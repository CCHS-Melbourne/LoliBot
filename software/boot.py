# This file is executed on every boot (including wake-boot from deepsleep)
#
# boot.py: version: 2018-01-20 00:45
#
# Usage
# ~~~~~
# pub() { mosquitto_pub -h $1 -t $2 -m "$3"; }
# AIKO_MQTT_HOST=iot.eclipse.org
# TOPIC=esp32/esp32_??????/in
# pub $AIKO_MQTT_HOST $TOPIC stop
# pub $AIKO_MQTT_HOST $TOPIC forward
# pub $AIKO_MQTT_HOST $TOPIC reverse
# pub $AIKO_MQTT_HOST $TOPIC left
# pub $AIKO_MQTT_HOST $TOPIC right

import aiko.led
import configuration.led
aiko.led.initialise(configuration.led.settings)
aiko.led.set(aiko.led.colors["red"], 0, True)

import lolibot
import configuration.lolibot
lolibot.initialise(configuration.lolibot.settings)

import aiko.wifi
import configuration.wifi
import time
while not aiko.wifi.connect(configuration.wifi.ssids): time.sleep(0.5)
aiko.led.set(aiko.led.colors["blue"], 0, True)

import configuration.mpu9250
import mpu9250
mpu9250.initialise(configuration.mpu9250.settings, lolibot.i2c_bus)

# import aiko.services
# import configuration.services
# aiko.services.initialise(configuration.services.settings)

import aiko.mqtt
import configuration.mqtt
settings = configuration.mqtt.settings
settings["topic_path"] += "/esp32_" + aiko.mqtt.get_unique_id()
settings["topic_subscribe"].append(settings["topic_path"] + "/in")
aiko.mqtt.initialise(settings)
aiko.mqtt.add_message_handler(aiko.led.on_message_led)
aiko.mqtt.add_message_handler(lolibot.on_message_lolibot)
# Handy to eval() Python, but a security risk !
# aiko.mqtt.add_message_handler(aiko.mqtt.on_message_eval)  # must be last
aiko.led.set(aiko.led.colors["green"], 0, True)

import udp_control
udp_control.initialise()
udp_control.add_message_handler(aiko.led.on_message_led)
udp_control.add_message_handler(lolibot.on_message_lolibot)

while True:
  aiko.mqtt.ping_check()        # TODO: Create a general timer handler
  mpu9250.accel_check()
  aiko.mqtt.client.check_msg()  # Then make this a blocking call
  udp_control.check()
