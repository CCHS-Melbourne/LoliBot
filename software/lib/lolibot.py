# lib/lolibot.py: version: 2018-01-19 23:15
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
# Topic: /in  {forward|stop|left|right|reverse}
#    - set the motors to a particular motion
# Topic: /in  freq FREQUENCY
#    - Set the motor PWM frequency
# Topic: /in  motors (A1 B2 A2 B2)
#    - Set a particular PWM config directly on the motor pins
#      for finer control
# Topic: /in servo [-100..100]
#    - Set the servo motion from -100 to 100 (0 = stopped)
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
servo = None

duty_cycle_max = 1023
duty_cycle_min = 200
pwm_frequency = 30

i2c_bus = None

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

def servo_pos(servo_duty):
  servo.duty(servo_duty)

def map_vals(val, min_in, max_in, min_out, max_out):
   return (val-min_in)/(max_in-min_in)*(max_out-min_out)+min_out

def on_message_lolibot(topic, payload_in):
  global pwm_frequency

  if payload_in in motor_commands:
    print("motor: " + payload_in)
    motor_action(motor_commands[payload_in])
    return True

  tokens = payload_in.split()
  if len(tokens) == 2 and tokens[0] == "freq":
    pwm_frequency = int(tokens[1])
    print("motor freq: " + str(pwm_frequency))
    return True

  if len(tokens) == 2 and tokens[0] == "servo":
    servo_position = map_vals(int(tokens[1]), -100, 100, 115, 40)
    print("Servo control to : " + str(servo_position))
    servo_pos(int (servo_position))
    return True

  if len(tokens) == 5 and tokens[0] == "motors":
    motor_settings = [int(x) for x in tokens[1:]]
    print("motor settings: {}".format(' '.join (tokens[1:])))
    motor_action(motor_settings)
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
  global servo
  global i2c_bus

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

  servo_pin = Pin(settings["servo_pin"], Pin.OUT)
  servo = PWM(servo_pin)
  servo.freq(50) # Set 50Hz PWM
  servo.duty(77) # Off

  scl = settings["scl_pin"]
  sda = settings["sda_pin"]
  i2c_bus = machine.I2C(scl=machine.Pin(scl), sda=machine.Pin(sda))
