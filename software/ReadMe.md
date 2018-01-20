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

## 1. Python development environment set-up

If you are already familar with and have Python and the PIP package installer
running on your development machine, then please move to step 2.  Otherwise,
depending upon your operating system, you'll have different steps to perform.

### Linux: Python and PIP

Batteries are included ... you are probably good to go.
Python and PIP are likely installed ... or you are reasonably self-sufficient.

### Mac OS X: Python and PIP

If you are a regular Python developer ... you'll be good to go.
If not, you'll have the default Apple Python installation (old) and no PIP.

Try ...

    sudo easy_install pip

If that fails, then using Homebrew to manage Python is the way to go ...

    brew install python  # Includes PIP

### Windows: Python and PIP

Oh dear, there is a little more effort required here.
Fortunately, Nick Moore has you covered with his
(detailed installation instructions)[https://github.com/nickzoic/mpy-tut/blob/master/tut/installing.md#windows-10] ... thanks Nick !

## 2. Install ESPTool (firmware installer)

    pip install esptool
    esptool.py -h    # ESP8266 ROM Bootloader Utility
    miniterm.py -h   # Simple low-level terminal program for the serial port

## 3. Install AMPY (file transfer utility)

    pip install adafruit-ampy
    ampy --help 
    AMPY_DELAY=1     # Workaround for reliable interaction with raw REPL

## 4. Install rshell (combined file transfer and microPython REPL interaction)

    pip install rshell
    rshell -h

# LoliBot (ESP32) microPython firmware installation

  http://micropython.org/downloads#esp32

# LoliBot (ESP32) microPython application installation

# Lolibot application overview
