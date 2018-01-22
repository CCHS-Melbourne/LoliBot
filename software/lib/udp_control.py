# lib/udp_control.py: version = "2018-01-22 17:00"
#
# Usage
# ~~~~~
# import udp_control
# udp_contro.initialise()
#
# while True:
#   udp_control.check()

import machine
import network
import time
import usocket

protocol = None
socket = None
message_handlers = []
time_last_cmd = -5000

ip_address = None
port = 4900

def initialise():
  global ip_address, socket

  sta_if = network.WLAN(network.STA_IF)
  ip_address = sta_if.ifconfig()[0]

  socket = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
  socket.bind((ip_address, port))
  socket.setblocking(False)

def add_message_handler(message_handler):
  message_handlers.append(message_handler)

def send_announce():
  global socket, port
  # print ("Bip")
  request = b"lolibot! {} {}".format (str(ip_address), port)
  address = ("255.255.255.255", port)
  socket.sendto(request, address)

def check():
  global socket

  # Send announcement on 5 second timeout
  global time_last_cmd
  time_now = time.ticks_ms()
  if time_now > time_last_cmd + 5000:
    send_announce()
    time_last_cmd = time_now

  try:
    response, addr = socket.recvfrom(1024)
    payload_in = response.decode("utf-8")
    messages = [x.strip() for x in payload_in.split('\n')]
    for message in messages:
      for message_handler in message_handlers:
        try:
          handled = message_handler('lolibot/udp/in', message)
          if handled: break
        except Exception as exception:
          print("UDP: handler {}({}) exception {} ".format (message_handler.__name__, message, str(exception)))
  except OSError:
    pass
