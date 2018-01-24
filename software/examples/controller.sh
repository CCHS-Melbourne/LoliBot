#!/bin/bash
# wtfpl by madduck, 2017
#
# ./controller.sh esp32_hexid
#
set -eu

ID="$1"

get_host() {
  PYTHONPATH="$(dirname $0)/../configuration" python -c "from mqtt import settings;print(settings['host'])"
}

lolibot_control() {
  mosquitto_pub -d -h "$(get_host)" -t lolibot/${ID}/in -m "$@"
}

trap "lolibot_control stop" EXIT

while read -rsn1 dir; do
  case "$dir" in
    (j) lolibot_control reverse;;
    (k) lolibot_control forward;;
    (h) lolibot_control left;;
    (l) lolibot_control right;;
    (q) break;;
    (*) lolibot_control stop;;
  esac
done
