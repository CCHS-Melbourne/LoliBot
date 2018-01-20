# LoliBot - Software Guide

Using and developing software for the LoliBot or any ESP32 microPython based
project requires a few command-line tools written in Python.  These tools
help load and manage the microPython firmware and your application source
code files on the ESP32 microcontroller.  One of the advantages of using
microPython is eliminating the need for a complex compiler tool-chain
and development environment on your host computer.  You may choose your
favorite source code editor and other utilities that best suit your needs.

# Development (host) computer software installation

The recommended tools are all written in Python.  If you are familar with
using Python virtual environments, it is recommended that you set-up a
specific virtual environment for ESP32 development.  However, you may
safely proceed without a Python virtual environment.

## 1. Install ESPTool (firmware installer)

    pip install esptool
    esptool.py -h    # ESP8266 ROM Bootloader Utility
    miniterm.py -h   # Simple low-level terminal program for the serial port

## 2. Install AMPY (file transfer utility)

    pip install adafruit-ampy
    ampy --help 
    AMPY_DELAY=1     # Workaround for reliable interaction with raw REPL

## 3. Install rshell (combined file transfer and microPython REPL interaction)

    pip install rshell
    rshell -h

# LoliBot (ESP32) microPython firmware installation

  http://micropython.org/downloads#esp32

# LoliBot (ESP32) microPython application installation

# Lolibot application overview
