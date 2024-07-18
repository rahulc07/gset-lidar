import os
import sys
import abd
from math import floor
from adafruit_rplidar import RPLidar

from douglas_peucker import  dp, check_pothole


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
            # TALK ABOUT CLENAING DATA
            if (scan[point][2] < 300):
                #print(scan[point][2])
                if not (scan[point][1] > 20 and scan[point][1] < 300):
                    point_cloud.append([scan[point][1], scan[point][2]])
        if len(point_cloud) >= 1:
            #print(len(abd.abd(point_cloud)))
            print(check_pothole(dp(abd.abd(point_cloud))))
        
    
except KeyboardInterrupt:
    print('Stopping.')
lidar.stop()
lidar.disconnect()