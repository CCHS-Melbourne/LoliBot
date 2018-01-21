# LoliBot - Software Guide

Using and developing software for the LoliBot or any ESP32 microPython based
project requires a few command-line tools written in Python.  These tools
help load and manage the microPython firmware and your application source
code files on the ESP32 microcontroller.  One of the advantages of using
microPython is eliminating the need for a complex compiler tool-chain
and development environment on your host computer.  You may choose your
favorite source code editor and other utilities that best suit your needs.

During the LCA2018 Open Hardware MiniConference (OHMC), we anticipate a
large variety of laptops, operating systems, Linux distributions and
personal preferences.  The following instructions aim to cover a
reasonable spread of environments, but we can't provide specific
step-by-step instructions for every situation.

**If you are having problems during the OHMC workshop, please ask
one of the organisers or friendly and experienced helpers for assistance**

The LoliBot software documentation is provided in three parts ...

- Development (host) computer software installation _(this page)_
- [LoliBot microPython software description](documentation/description.md)
- [LoliBot end-to-end examples](documentation/end-to-end.md)

# Development (host) computer software installation

The recommended tools are all written in Python.  If you are familar with
using Python virtual environments, it is recommended that you set-up a
specific virtual environment for ESP32 development.  However, you may
safely proceed without a Python virtual environment.

## 1. Python development environment set-up

If you are already familar with and have Python and the PIP package installer
running on your development machine, then please move to step 2.  Otherwise,
depending upon your operating system, you'll have different commands to perform.

### Linux: Python and PIP

Batteries are included ... you are probably good to go.
Python and PIP are likely installed ... or if not, you are reasonably
self-sufficient and are comfortable with updating your personal choice
of Linux distribution.  We are hoping these are not bad assumptions !

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
The ESP32 development board chosen for the LoliBot is the
[Wemos Lolin32 Lite](https://wiki.wemos.cc/products:lolin32:lolin32_lite).
The Wemos Lolin32 Lite uses the CH340 USB serial interface chip.

If you are already familar with developing for embedded computers,
then you are likely on top of the USB serial driver and configuration
required on your development machine.

### Linux: USB serial driver is probably included

Many Linux distributions already include the CH340 USB serial driver.
However, you may need to give yourself permission to access the serial device.

    usermod -a -G dialout $USER
    id | grep dialout  # Check if your user is in the "dialout" group

You may need to log out and then log back in again for this change to
have effect.

When you plug your LoliBot (ESP32) into the USB port, it should appear as
"/dev/ttyUSB0" (or similar).

    ls -l /dev/ttyUSB*  # Check if LoliBot appears as a serial device

### Mac OS X: USB serial driver needs to be installed

Mac OS X requires the CH340 USB serial driver.
However, you may have installed the driver previously.
If you plug your LoliBot into the USB port ...
and you can see the file "/dev/tty.wchusbserial1410" (or similar)
then you can move on to the next step.

    ls -l /dev/tty.wchusbserial*  # Check if LoliBot appears as a serial device

Otherwise, install the [Mac OS X CH340 driver](https://wiki.wemos.cc/downloads)
Finally, test plugging in the LoliBot and look for the serial device as above.

### Windows: USB serial driver needs to be installed

Once again, [Nick Moore's documentation](https://github.com/nickzoic/mpy-tut/blob/master/tut/installing.md#windows-10) comes to the rescue.
Follow those instructions and then ... just go buy Nick a beer !

You can get the Windows CH340 driver from
[here](https://wiki.wemos.cc/downloads) or
[there](http://www.wch.cn/download/CH341SER_EXE.html)

## 3. Install ESPTool (firmware installer with miniterm.py)

The ESPtool package allows you to install firmware, such as the microPython
interpreter, on to your ESP32 microcontroller.  This package also contains
the "miniterm.py" utility, which acts like a serial terminal console that
allows REPL (shell-like) access to microPython running on your ESP32.

    pip install esptool
    esptool.py -h    # ESP8266 ROM Bootloader Utility

    miniterm.py -h   # Simple low-level terminal program for the serial port

Note: Other good serial terminal choices, besides "miniterm.py" are ...

- Linux or Mac OS X: "screen"
- Windows: ["putty"](http://chiark.greenend.org.uk/~sgtatham/putty/latest.html)

Make sure your serial terminal is configured to run at 115,200 baud and with
"flow control" disabled (or set to "none").

## 4. Install AMPY (file transfer utility)

The AMPY utility allows you to inspect the microPython filesystem, send and
retrieve files, make directories and delete files or directories.

    pip install adafruit-ampy
    AMPY_DELAY=1     # Workaround for reliable interaction with raw REPL
    ampy --help 

If "ampy" is hanging or crashing, ensure that the AMPY_DELAY environment
variable is set to the value "1".  Also, double-check that the ESP32 serial
device exists and the path is correct, as follows ...

    ls -l /dev/tty.wchusbserial*
    echo $AMPY_PORT

... both should be the same file pathname.

Note: AMPY_DELAY appears to be needed for the Wemos Lolin32 Lite.
Other ESP32 development boards, often those that don't use the CH340,
don't need the AMPY_DELAY environment variable and are better off
without it.

## 5. Install rshell (combined file transfer and microPython REPL interaction)

The installation of "rshell" is optional.  It relies upon Python version 3.4
or higher.  This utility combines the functionality a serial terminal and
"ampy".  It is worth trying out.  However, "rshell" works less well on the
Wemos Lolin32 Lite.  So, you might be better trying it out on different ESP32
device that doesn't use a CH340 USB serial chip ... before making up your mind.

    pip install rshell
    rshell -h

---
This concludes the development (host) computer software installation.
Now let's use these development tools to set-up microPython on the ESP32.
---
