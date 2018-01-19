# lib/aiko/mqtt.py: version = "2018-01-19 23:00"
#
# Usage
# ~~~~~
# import aiko.mqtt
# import configuration.mqtt
# settings = configuration.mqtt.settings
# settings["topic_path"] += "/esp32_" + aiko.mqtt.get_unique_id()
# settings["topic_subscribe"].append(settings["topic_path"] + "/in")
# aiko.mqtt.initialise(settings)
# aiko.mqtt.add_message_handler(aiko.mqtt.on_message_eval)  # must be last
#
# while True:
#   aiko.mqtt.ping_check()
#   aiko.mqtt.client.check_msg()

import gc
import machine
import time

from umqtt.robust import MQTTClient

client = None
keepalive = 60
message_handlers = []
ping_counter = 0
time_last_ping = 0
state_topic = None

def add_message_handler(message_handler):
  message_handlers.append(message_handler)

def get_unique_id():
  id = machine.unique_id()
  id = ("000000" + hex((id[3] << 16) | (id[4] << 8) | id[5])[2:])[-6:]
  return id

def on_message(topic, payload_in):
  topic = topic.decode()
  payload_in = payload_in.decode()

  for message_handler in message_handlers:
    try:
      handled = message_handler(topic, payload_in)
      if handled: break
    except Exception as exception:
      print("MQTT: handler {}() exception {} ".format (message_handler.__name__, str(exception)))

def on_message_eval(topic, payload_in):
  try:
    eval(payload_in)
  except Exception as exception:
    print("MQTT: eval(): " + str(exception))
  return True

def set_state(state_msg):
  global client, state_topic
  client.publish(state_topic, state_msg, retain=True)

def ping_check():
  global ping_counter, time_last_ping
  time_now = time.ticks_ms()
  if time_now > time_last_ping + 1000:
    time_last_ping = time_now

    ping_counter -= 1
    if ping_counter < 1:
      ping_counter = keepalive
      client.ping()
      gc.collect()
      print("GC:", gc.mem_free(), gc.mem_alloc())   # 72272 23728

def initialise(settings):
  global client, keepalive, state_topic

  client_id = get_unique_id()
  keepalive = settings["keepalive"]
  topic_path = settings["topic_path"]
  state_topic = topic_path + "/state"

  client = MQTTClient(client_id,
    settings["host"], settings["port"], keepalive=keepalive)

  client.set_callback(on_message)
  client.set_last_will(state_topic, "nil")
  client.connect()

  for topic in settings["topic_subscribe"]: client.subscribe(topic)

  set_state ("alive")

  print("Connected to MQTT: %s: %s" % (settings["host"], topic_path))
