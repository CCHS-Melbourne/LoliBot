#!/bin/bash
# wtfpl by madduck, 2017
#
# ./controller.sh esp32_hexid
#
set -eu

ID="$1"

lolibot_control() {
  mosquitto_pub -d -h iot.eclipse.org -t lolibot/${ID}/in -m "$@"
}

while read -rsn1 dir; do
  case "$dir" in
    (x) lolibot_control stop;;
    (j) lolibot_control reverse;;
    (k) lolibot_control forward;;
    (h) lolibot_control left;;
    (l) lolibot_control right;;
    (q) break;;
  esac
done
