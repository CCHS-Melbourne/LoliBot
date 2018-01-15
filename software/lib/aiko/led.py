# lib/aiko/led.py: version = "2018-01-16 09:00"
#
# Usage
# ~~~~~
# import aiko.led
# import configuration.led
# aiko.led.initialise(configuration.led.settings)
# aiko.led.set(aiko.led.colors["red"], 0, True)
#
# After setting up aiko.wifi and aiko.mqtt, then ...
#   aiko.mqtt.add_message_handler(aiko.led.on_message_led)
#
# MQTT commands
# ~~~~~~~~~~~~~
# Topic: /in   (led:clear)
#              (led:line  R G B X0 Y0 X1 Y1)
#              (led:set   R G B X)
#              (led:write)
#              (led:write R G B ...)
#
# Topic: /in   (led:traits)
#        /out  (led:traits rgb LED_COUNT)

from machine  import Pin
from neopixel import NeoPixel

import urandom
apa106   = False
dim      = 0.1  # 100% = 1.0
full     = 255
length   = None
length_x = None
np       = None
zigzag   = False

colors = {
  "black":  (   0,    0,    0),
  "red":    (full,    0,    0),
  "green":  (   0, full,    0),
  "blue":   (   0,    0, full),
  "purple": (full,    0, full),
  "yellow": (full, full,    0),
  "white":  (full, full, full)
}

def apply_dim(color, dimmer=None):
  if dimmer == None: dimmer = dim
  return tuple([int(element * dimmer) for element in color])

# Bresenham's line algorithm
def line(color, x0, y0, x1, y1):
  x_delta = abs(x1 - x0);
  y_delta = abs(y1 - y0);
  x_increment = 1 if x0 < x1 else -1
  y_increment = 1 if y0 < y1 else -1
  error = (y_delta if y_delta > x_delta else -x_delta) / 2

  while True:
    set_xy(color, x0, y0)
    if y0 == y1 and x0 == x1: break
    error2 = error

    if error2 > -y_delta:
      error -= x_delta
      y0 += y_increment

    if error2 < x_delta:
      error += y_delta
      x0 += x_increment

def linear(dimension):
  if type(dimension) == int: return dimension
  result = 1
  for index in range(len(dimension)): result *= dimension[index]
  return result

def random_color():
  red   = urandom.randint(0, full)
  green = urandom.randint(0, full)
  blue  = urandom.randint(0, full)
  return (red, green, blue)

def random_position():
  return urandom.randint(0, length - 1)

def set(color, x=0, write=False):
  if apa106: color = (color[1], color[0], color[2])
  if zigzag and (x // length_x) % 2:
    x = length_x * (x // length_x + 1) - (x - length_x * (x // length_x)) - 1
  if x < length: np[x] = apply_dim(color)
  if write: np.write()

def set_random_pixel(write=False):
  set(random_color(), random_position(), write)

def set_xy(color, x=0, y=0, write=False):
  set(color, x + y * length_x, write)

def initialise(settings):
  global apa106, length, length_x, np, zigzag

  length = linear(settings["dimension"])
  length_x = settings["dimension"][0]
  np = NeoPixel(Pin(settings["neopixel_pin"]), length, timing=True)
  if "apa106" in settings: apa106 = settings["apa106"]
  if "zigzag" in settings: zigzag = settings["zigzag"]

def on_message_led(topic, payload_in):
  if payload_in == "(led:clear)":
    np.fill(colors["black"])
    np.write()
    return True

  if payload_in.startswith("(led:dim "):
    global dim
    tokens = [float(token) for token in payload_in[9:-1].split()]
    dim = tokens[0]
    return True

  if payload_in.startswith("(led:set "):
    tokens = [int(token) for token in payload_in[9:-1].split()]
    set((tokens[0], tokens[1], tokens[2]), tokens[3])
    return True

  if payload_in.startswith("(led:line "):
    tokens = [int(token) for token in payload_in[10:-1].split()]
    color = (tokens[0], tokens[1], tokens[2])
    line(color, tokens[3], tokens[4], tokens[5], tokens[6])
    return True

  if payload_in.startswith("(led:write"):
    tokens = [int(token) for token in payload_in[11:-1].split()]
    offset = 0
    for position in range(0, len(tokens) / 3):
      color = (tokens[offset], tokens[offset + 1], tokens[offset + 2])
      set(color, position)
      offset += 3
    np.write()
    return True

# if payload_in == "(led:traits)":
#   payload_out  = "(traits rgb " + str(LED_COUNT) + ")"
#   mqtt_client.publish(TOPIC_OUT, payload_out)
#   return True

  return False
