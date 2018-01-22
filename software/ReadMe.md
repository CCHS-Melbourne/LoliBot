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
- WILL EXIST SOON ... [LoliBot microPython software description](documentation/description.md)
- WILL EXIST SOON ... [LoliBot end-to-end examples](documentation/end-to-end.md)

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

If that fails, then using [Homebrew](https://brew.sh) to install and manage
Python is the way to go.  Note: This will take awhile, e.g a coffee break.

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
then you can move on to the next step 3.

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

The ESPTool package allows you to install firmware, such as the microPython
interpreter, on to your ESP32 microcontroller.  This package also contains the
"miniterm.py" program, which acts like a serial terminal console that allows
[REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
(shell-like) access to microPython running on your ESP32.

    pip install esptool
    esptool.py -h    # ESP8266 ROM Bootloader Utility

    miniterm.py -h   # Simple low-level terminal program for the serial port

Note: Other good serial terminal choices, besides "miniterm.py" are ...

- Linux or Mac OS X: screen
- Windows: [putty](http://chiark.greenend.org.uk/~sgtatham/putty/latest.html)

Make sure your serial terminal is configured to run at 115,200 baud and with
"flow control" disabled (or set to "none").

## 4. Install AMPY (file transfer program)

The [ampy](https://github.com/adafruit/ampy) program allows you to inspect
the microPython filesystem, send and retrieve files, make directories and
delete files or directories.

    pip install adafruit-ampy
    ampy --help
    AMPY_DELAY=1     # Workaround for reliable interaction with raw REPL
    AMPY_PORT=/dev/ttyUSB0               # Linux
    AMPY_PORT=/dev/tty.wchusbserial1410  # Mac OS X
    set AMPY_PORT=COM3                   # Windows

If "ampy" is hanging or crashing, ensure that the AMPY_DELAY environment
variable is set to the value "1".  Also, double-check that the ESP32 serial
device exists and that the path is correct, as follows ...

    ls -l /dev/tty.wchusbserial*
    echo $AMPY_PORT

... both should be the same device file pathname.

Note: AMPY_DELAY appears to be needed for the Wemos Lolin32 Lite.
Other ESP32 development boards, often those that don't use the CH340,
don't need the AMPY_DELAY environment variable and are better off
without it.

## 5. Install rshell (combined file transfer and microPython REPL interaction)

The installation of "rshell" is optional.  It relies upon Python version 3.4
or higher.  This program combines the functionality of a serial terminal and
"ampy".  It is worth trying out.  However, "rshell" works less well on the
Wemos Lolin32 Lite.  So, you might be better trying it out on a different ESP32
development board that doesn't use a CH340 USB serial chip ... before making up
your mind about whether you like using "rshell".

    pip install rshell
    rshell -h

Another similar program to try out is
[mpfshell](https://github.com/wendlers/mpfshell).

---

This concludes the development (host) computer software installation.
Now let's use these development tools to set-up microPython on the ESP32.

---

# LoliBot (ESP32) microPython firmware installation

The microPython firmware is installed on the ESP32 using ESPTool to
erase the microcontroller flash memory and then write the firmware image.

The latest version of the microPython firmware image can be found here ...

    http://micropython.org/downloads#esp32

A recent firmware version (January 2018) has been included as part of
this repository.

The required ESPTool commands ...

    esptool.py --chip esp32 --port $AMPY_PORT erase_flash
    esptool.py --chip esp32 --port $AMPY_PORT write_flash -z 0x1000 firmware/esp32-20180120-v1.9.3-240-ga275cb0f.bin

... can be more conveniently run in a shell script that completely installs
all of the LoliBot software (see next section).

Once the microPython firmware image is installed, you can reboot the ESP32
and use a serial terminal program to enter and execute Python statements
interactively at the ">>>" prompt.  **This is very cool !**  It enables
you to play, experiment and diagnose problems in an easy, yet powerful
manner.

# LoliBot (ESP32) microPython application installation

By this stage, we are now ready to install the complete collection
of software that will operate your LoliBot hardware.

**To prevent accidental robot run-aways, ensure that the LoliBot power
switch is OFF** ... or that you have excellent robot catching reflexes !

The following commands flash the microPython firmware and copy the entire
LoliBot software to the ESP32.  This is also a convenient "one step" command
to get your LoliBot back into a known state, if you've made lots of ad-hoc
"ampy put" commands and have forgotten exactly what is installed on the ESP32.

    export AMPY_DELAY=1
    export AMPY_PORT=/dev/ttyUSB0               # Linux
    export AMPY_PORT=/dev/tty.wchusbserial1410  # Mac OS X
    set AMPY_PORT=COM3                          # Windows
    scripts/flash_lolibot.sh  # Takes around 2 to 3 minutes ... grab a coffee !

Since all the LoliBot source files have a "version header" ... the following
script uses "ampy get" to retrieve the microPython source files from the
ESP32 and display just the "version header" for each file for the purposes
of checking.

    scripts/check_version.sh

# Configure LoliBot Wi-Fi

The final installation steps are to configure the LoliBot settings
for Wi-Fi and MQTT.

**So that you can see the RGB LED boot status, ensure that the LoliBot
power switch is ON.  Raise the LoliBot wheels off the ground, then
the robot can't accidentally run away from you.**  Due to the design,
whenever the ESP32 microcontroller is "reset", the motors tend to
consistently run for just under a second.

The default LoliBot RGB LED boot behavior is as follows ...

- Red: Waiting for Wi-Fi connection
- Blue: Wi-Fi connected, waiting for MQTT connection
- Green: Wi-Fi connected and MQTT connected, ready to go

Failure of the RGB LED to progress from _red_ to _blue_ to _green_ indicates
that some sort of problem has occurred.  Possibly, the Wi-FI network
credentials are incorrect.

Copy, edit and transfer the Wi-Fi configuration file ...

    cp configuration/wifi.py.template configuration/wifi.py
    vi configuration/wifi.py
      ssids = [
        ("linuxconfau", "??????????")
      ]
    ampy put configuration/wifi.py configuration/wifi.py

Note: Both "ampy" and "miniterm.py" (or any serial terminal program)
can not be run at the same time, otherwise they contend for the same
USB serial device port.  So, always stop your serial terminal program
before running the "ampy" command.

Whilst watching the serial console output, reboot the ESP32,
by pressing the "reset" button

    miniterm.py $AMPY_PORT 115200

Example: Successful Wi-Fi connection console output.
Note: RGB LED should start _red_ and change to _blue_.

    (979) wifi: STA_START
    (3389) network: event 1
    Connecting to meshthing
    Waiting for Wi-Fi
    (4819) wifi: n:11 0, o:1 0, ap:255 255, sta:11 0, prof:1
    (5379) wifi: state: init -> auth (b0)
    (5379) wifi: state: auth -> assoc (0)
    (5389) wifi: state: assoc -> run (10)
    (5409) wifi: connected with meshthing, channel 11
    (5409) network: event 4
    (8389) wifi: pm start, type:0
    (9349) event: sta ip: 192.168.1.5, mask: 255.255.255.0, gw: 192.168.1.1
    (9349) network: GOT_IP
    Connected to Wi-Fi

Example: Failure to connect to Wi-Fi, due to incorrect SSID.
Note: RGB LED stays _red_.  Edit and transfer "configuration/wifi.py",
then try rebooting again.

    (998) wifi: STA_START
    (3408) network: event 1
    (6418) network: event 1

Example: Failure to connect to Wi-Fi, due to incorrect password.
Note: RGB LED stays _red_.  Edit and transfer "configuration/wifi.py",
then try rebooting again.

    (979) wifi: STA_START
    (3389) network: event 1
    Connecting to meshthing
    Waiting for Wi-Fi
    (4819) wifi: n:11 0, o:1 0, ap:255 255, sta:11 0, prof:1
    (5379) wifi: state: init -> auth (b0)
    (5389) wifi: state: auth -> assoc (0)
    (6389) wifi: state: assoc -> init (4)
    (6389) wifi: n:11 0, o:11 0, ap:255 255, sta:11 0, prof:1
    (6389) wifi: STA_DISCONNECTED, reason:4

Note: Typically, when a serial terminal program, such as "miniterm.py",
is started ... it will "reset" the ESP32.

# Configure LoliBot MQTT

Once the LoliBot is successfully connecting to the Wi-Fi network,
it is time to configure MQTT.

There are a couple of options ...

- Connect to a third-party hosted, public MQTT server, such as
  - "iot.eclipse.org"
  - "test.mosquitto.org"
- Connect to a local MQTT server running on your laptop

Copy, edit and transfer the MQTT configuration file ...

    vi configuration/mqtt.py
      "host": "iot.eclipse.org",  # Third-party hosted, public MQTT server
    # "host": "192.168.1.4"       # Local MQTT server
    ampy put configuration/mqtt.py configuration/mqtt.py

Whilst watching the serial console output, reboot the ESP32,
by pressing the "reset" button

    miniterm.py $AMPY_PORT 115200

Example: Successful MQTT connection console output.
Note: RGB LED should start _red_, change to _blue_ and then _green_.

    (998) wifi: STA_START
    (3408) network: event 1
    Connecting to meshthing
    Waiting for Wi-Fi
    (4828) wifi: n:11 0, o:1 0, ap:255 255, sta:11 0, prof:1
    (5388) wifi: state: init -> auth (b0)
    (5388) wifi: state: auth -> assoc (0)
    (5388) wifi: state: assoc -> run (10)
    (5408) wifi: connected with meshthing, channel 11
    (5418) network: event 4
    (8388) wifi: pm start, type:0
    (9368) event: sta ip: 192.168.1.6, mask: 255.255.255.0, gw: 192.168.1.1
    (9368) network: GOT_IP
    Connected to Wi-Fi
    (9718) modsocket: Initializing
    Connected to MQTT: 192.168.1.2: lolibot/esp32_000000

Example: Failure to connect to MQTT, due to incorrect MQTT host IP address.
Note: RGB LED starts _red_ and then stays _blue_.
Edit and transfer "configuration/mqtt.py", then try rebooting again.

    Connected to Wi-Fi
    (9718) modsocket: Initializing
    Traceback (most recent call last):
      File "boot.py", line 40, in <module>
      File "/lib/aiko/mqtt.py", line 77, in initialise
      File "/lib/umqtt/simple.py", line 58, in connect
    OSError: [Errno 104] ECONNRESET
    OSError: [Errno 2] ENOENT

---

Now that your LoliBot is connected to Wi-Fi and MQTT, it is time to move on to
[LoliBot microPython software description](documentation/description.md) ... WILL EXIST SOON
