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
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME, timeout=3, baudrate=100000)

# used to scale data to fit on the screen
max_distance = 0

scan_data = [0]*360
lidar.set_pwm(255)
counter = 1
joined_point_cloud=[]
try:
    print(lidar.info)

    point_cloud=[]
    for scan in lidar.iter_scans():
        print("GOOOO")
        # Clean/Filter the data
        for point in range(len(scan)):
            if (scan[point][2] < 1000) and ((scan[point][1] < 60) or (scan[point][1] > 300)):
                point_cloud.append([scan[point][1], scan[point][2]])
        #print(point_cloud)
        if len(point_cloud) >= 1:
            lines = dp(abd.abd(point_cloud))
            #check_pothole(lines)
            if counter % 10 == 0:
                if check_pothole(lines):
                    print(convex_hull_volume(convert_to_3d(joined_point_cloud)))
                lidar.stop()
                lidar.disconnect()
                sys.exit()
            else:
                print(counter)
                joined_point_cloud = joined_point_cloud + point_cloud  
            counter+=1

            
        
    
except KeyboardInterrupt:
    print('Stopping.')
lidar.stop()
lidar.disconnect()