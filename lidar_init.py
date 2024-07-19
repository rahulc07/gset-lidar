# %%
import os
import sys
import abd
from math import floor
from adafruit_rplidar import RPLidar

from convert_to_3d_cloud import convert_to_3d
from convex_hull import convex_hull_volume
from douglas_peucker import  dp, check_pothole


# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB1'
lidar = RPLidar(None, PORT_NAME, timeout=3)

# used to scale data to fit on the screen
max_distance = 0

scan_data = [0]*360
lidar.set_pwm(255)
counter = 0
try:

    #print(lidar.info)
    for scan in lidar.iter_scans():
        point_cloud=[]
        # This will go out of scope after every scan
        for point in range(len(scan)):
            # TALK ABOUT CLENAING DATA
            if (scan[point][2] < 700):
                print(scan[point])
                if not (scan[point][1] > 45) or not (scan[point][1] < 315):
                    point_cloud.append([scan[point][1], scan[point][2]])
        print(point_cloud)
        if len(point_cloud) >= 1:
            print(len(abd.abd(point_cloud)))
            lines = dp(abd.abd(point_cloud))
            if (check_pothole(lines)):
                print(convex_hull_volume(convert_to_3d(point_cloud)))
            
        
    
except KeyboardInterrupt:
    print('Stopping.')
lidar.stop()
lidar.disconnect()