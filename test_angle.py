import os
import sys
import abd
from math import floor
from adafruit_rplidar import RPLidar


# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME, timeout=3)

# used to scale data to fit on the screen
max_distance = 0

scan_data = [0]*360
lidar.set_pwm(255)
counter = 0
try:

    #print(lidar.info)
    for scan in lidar.iter_scans():
        # This will go out of scope after every scan
        point_cloud = []
        for point in range(len(scan)):
            if scan[point][2] < 270 and scan[point][2] > 230:
                print(scan[point][1])
        
    
except KeyboardInterrupt:
    print('Stopping.')
lidar.stop()
lidar.disconnect()