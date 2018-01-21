# LoliBot - Software Guide

Using and developing software for the LoliBot or any ESP32 microPython based
project requires a few command-line tools written in Python.  These tools
help load and manage the microPython firmware and your application source
code files on the ESP32 microcontroller.  One of the advantages of using
microPython is eliminating the need for a complex compiler tool-chain
and development environment on your host computer.  You may choose your
favorite source code editor and other utilities that best suit your needs.

During the LCA2018 Open Hardware MiniConference (OHMC), we anticipate a
large variety of machines, operating systems, Linux distributions and
personal preferences in their set-up.  The following instructions aim
to cover a reasonable spread of environments, but we can't provide
specific step-by-step instructions for every situation.

*If you are having problems during the OHMC workshop, please ask
one of the organisers or friendly and experienced helpers for assistance*

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
Python and PIP are likely installed ... or you are reasonably self-sufficient
and are comfortable with your personal choice of Linux distribution.

### Mac OS X: Python and PIP

If you are a regular Python developer ... you'll be good to go.
If not, you'll have the default Apple Python installation (old) and no PIP.

    sudo easy_install pip

If that fails, then using Homebrew to install and manage Python
is the way to go.  Note: This will take awhile, e.g a coffee break.

    brew install python  # Includes PIP (maybe called "pip2")

### Windows: Python and PIP

Oh dear, there is a little more effort required here.
Fortunately, Nick Moore has you covered with his
[detailed installation instructions](https://github.com/nickzoic/mpy-tut/blob/master/tut/installing.md#windows-10) ... thanks Nick !

## 2. Install USB serial driver (if required)

Development interaction with the ESP32 occurs over a USB serial connection.
The ESP32 development board chosen for the Lolibot is the
[Wemos Lolin32 Lite](https://wiki.wemos.cc/products:lolin32:lolin32_lite).
The Wemos Lolin32 Lite uses the CH340 USB serial interface chip.

If you are already familar with developing for embedded computers,
then you are likely on top of the USB serial driver and configuration
required on your development machine.

### Linux: USB serial driver is probably included

Most Linux distributions already include the CH340 USB serial driver.
However, you may need to give yourself permission to access the serial device.

    sudo adduser $USER dialout
    id | grep dialout  # Check if your user is in the "dialout" group

You may need to log out and then log back in again for this change to
have effect.

When you plug your LoliBot (ESP32) into the USB port, it should appear as
"/dev/ttyUSB0" (or similar).

    ls -l /dev/ttyUSB*

### Mac OS X: USB serial driver needs to be installed

Mac OS X requires the CH340 USB serial driver.
However, you may have installed the driver  previously.
If you plug your LoliBot into the USB port ...
if you can see the file "/dev/tty.wchusbserial1410" (or similar)
then you can move on to the next step.

    ls -l /dev/tty.wchusbserial*

Otherwise, install the [Mac OS X CH340 driver](https://wiki.wemos.cc/downloads)
Finally, test plugging in the LoliBot and look for the serial device as above.

### Windows: USB serial driver needs to be installed

Once again, [Nick Moore's documentation](https://github.com/nickzoic/mpy-tut/blob/master/tut/installing.md#windows-10) comes to the rescue ... just go buy him
a beer !

You can get the Windows CH340 driver from
[here](https://wiki.wemos.cc/downloads) or
[there](http://www.wch.cn/download/CH341SER_EXE.html)

## 3. Install ESPTool (firmware installer)

    pip install esptool
    esptool.py -h    # ESP8266 ROM Bootloader Utility
    miniterm.py -h   # Simple low-level terminal program for the serial port

## 4. Install AMPY (file transfer utility)

    pip install adafruit-ampy
    ampy --help 
    AMPY_DELAY=1     # Workaround for reliable interaction with raw REPL

## 5. Install rshell (combined file transfer and microPython REPL interaction)

Optional: Requires Python 3.4 or newer.

    pip install rshell
    rshell -h

# LoliBot (ESP32) microPython firmware installation

  http://micropython.org/downloads#esp32

# LoliBot (ESP32) microPython application installation

# Lolibot application overview
