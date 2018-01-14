# lib/lolibot.py: version: 2018-01-14 14:00
#
# Usage
# ~~~~~
# import lolibot
# import configuration.lolibot
# lolibot.initialise(configuration.lolibot.settings)
#
# After setting up aiko.wifi and aiko.mqtt, then ...
#   aiko.mqtt.add_message_handler(lolibot.on_message_lolibot)
#
# MQTT commands
# ~~~~~~~~~~~~~
# Topic: /in  freq FREQUENCY
#
# REPL testing
# ~~~~~~~~~~~~
# ma = lolibot.motor_action
# mc = lolibot.motor_commands
# mfl1 = lolibot.left_motor1.freq
# mfl1(30)
# l = (200, 0, 1023, 0)  # left
# ma(l)
# s = (0, 0, 0, 0)  # stop
# ma(s)

import machine
from machine import Pin
from machine import PWM

left_motor1 = None
left_motor2 = None
right_motor1 = None
right_motor2 = None

duty_cycle_max = 1023
duty_cycle_min = 200
pwm_frequency = 30

motor_commands = {
  "stop":    (   0,    0,    0,    0),
  "forward": (1023,    0, 1023,    0),
  "left":    ( 200,    0, 1023,    0),
  "right":   (1023,    0,  200,    0),
  "reverse": (   0, 1023,    0, 1023)
}

def motor_action(motor_command):
  left_motor1.duty(motor_command[0])
  left_motor2.duty(motor_command[1])
  right_motor1.duty(motor_command[2])
  right_motor2.duty(motor_command[3])

def on_message_lolibot(topic, payload_in):
  global pwm_frequency

  if payload_in in motor_commands:
    print("motor: " + payload_in)
    motor_action(motor_commands[payload_in])
    return True

  tokens = payload_in.split()
  if len(tokens) == 2 and tokens[0] == "freq":
    pwm_frequency = int(tokens[1])
    print("motor freq: " + int(pwm_frequency))
    return True

  return False

def initialise_motor(settings, motor_pin_name):
  motor = PWM(Pin(int(settings[motor_pin_name])))
  motor.freq(pwm_frequency)
  motor.duty(0)
  return motor

def initialise(settings):
  global duty_cycle_max, duty_cycle_min, pwm_frequency
  global left_motor1, left_motor2, right_motor1, right_motor2

  if "duty_cycle_max" in settings:
    duty_cycle_max = int(settings["duty_cycle_max"])
  if "duty_cycle_min" in settings:
    duty_cycle_min = int(settings["duty_cycle_min"])
  if "pwm_frequency" in settings:
    pwm_frequency = int(settings["pwm_frequency"])

  left_motor1 = initialise_motor(settings, "left_motor_pin1")
  left_motor2 = initialise_motor(settings, "left_motor_pin2")
  right_motor1 = initialise_motor(settings, "right_motor_pin1")
  right_motor2 = initialise_motor(settings, "right_motor_pin2")

  servo = Pin(settings["servo_pin"], Pin.OUT)

  scl = settings["scl_pin"]
  sda = settings["sda_pin"]
