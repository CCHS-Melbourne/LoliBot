# lib/aiko/wifi.py: version = "2018-01-14 14:00"
#
# Usage
# ~~~~~
# import aiko.wifi
# import configuration.wifi
# import time
# while not aiko.wifi.connect(configuration.wifi.ssids): time.sleep(0.5)

import network
import time

# Parameter(s)
#   ssids: List of tuples, each one containing the Wi-Fi AP SSID and password
#
# Returns boolean: Wi-Fi connected flag

def connect(ssids):
  sta_if = network.WLAN(network.STA_IF)
  sta_if.active(True)
  aps = sta_if.scan()

  for ap in aps:  # Note 1
    for ssid in ssids:
      if ssid[0].encode() in ap:
        print("Connecting to " + ssid[0])
        sta_if.connect(ssid[0], ssid[1])
        print("Waiting for Wi-Fi")
        while sta_if.isconnected() == False: time.sleep(0.1)  # Note 2
        print("Connected to Wi-Fi")
        break  # inner loop
    if sta_if.isconnected(): break  # outer loop

  return sta_if.isconnected()
