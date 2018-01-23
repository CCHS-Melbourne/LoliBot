# mpu9250.py: version: 2018-01-20 00:45
import struct
import math
import time

mpu = None

time_last_check = 0
maxZ = -50.0
minZ = 50.0

class MPU9250Exception(Exception):
    pass

class MPU9250:
    """support for the MPU-9250"""

    FS_2G = 0
    FS_4G = 8
    FS_8G = 16
    FS_16G = 24

    def __init__(self, bus, accel_max_g=2, addr=0x68):
        self.bus = bus
        self.addr = addr

        try:
           b = self.bus.readfrom_mem(self.addr, 0x75, 1)
        except OSError:
           raise MPU9250Exception("mpu9250 not detected.")

        if b[0] != 0x71:
            raise MPU9250Exception("Device that is not mpu9250 detected. WhoAmI reg contained 0x{:x}".format(b[0]))

        if accel_max_g <= 2:
            accel_fs_sel = 0
            self.accel_scale = 16384
        elif accel_max_g <= 4:
            accel_fs_sel = 8
            self.accel_scale = 8192
        elif accel_max_g <= 8:
            accel_fs_sel = 16
            self.accel_scale = 4096
        elif accel_max_g <= 16:
            accel_fs_sel = 24
            self.accel_scale = 2048
        else:
            raise ValueError("accel_max_g must be <= 16")

        self.bus.writeto_mem(self.addr, 0x6b, bytes([0]))
        self.bus.writeto_mem(self.addr, 0x1c, bytes([accel_fs_sel]))

    def update(self):
        # (ax, ay, az, _, gx, gy, gz) = self.readings
        self.readings = struct.unpack(">7h", self.bus.readfrom_mem(self.addr,0x3b,14))

    def readZ(self):
        # Returns a tuple of Z acceleration and Gyro reading
        self.update()

        az = self.readings[2]
        gz = self.readings[6]
        #return math.sqrt(ax*ax + ay*ay + az*az) / self.accel_scale, math.sqrt(gx*gx + gy*gy + gz*gz)
        return az / self.accel_scale, gz

def initialise(settings, i2c_bus):
    global mpu

    try:
        mpu = MPU9250(i2c_bus, settings["accel_max_g"], settings["i2c_addr"])
        print("MPU9250 initialised")
    except MPU9250Exception:
        print("MPU9250 module not detected.")

def readZ():
    if mpu:
        return mpu.readZ()
    return (0,0)

# FIXME: Replace with general timer implementation
def accel_check():
    global time_last_check, maxZ, minZ

    if mpu is None:
        return

    # Track the max/min accelerometer reading between updates
    # and output them once per second
    curZ = readZ()
    maxZ = max(curZ[0], maxZ)
    minZ = min(curZ[0], minZ)

    time_now = time.ticks_ms()
    if time_now >= time_last_check + 1000:
        time_last_check = time_now
        print ("Accel Z {} min {} max {}".format(readZ(), minZ, maxZ))
        minZ = 50.0
        maxZ = -50.0
