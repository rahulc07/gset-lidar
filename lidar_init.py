from adafruit_rplidar import RPLidar
import os


PORT = '/dev/ttyUSB0'
lidar = RPLidar(NONE, PORT)
# scan_data[angle] = distance
angle_mount = 45
scan_data = [0] * 360
    

try:
    print(lidar.info)
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan
        scandata[min(359, floor(angle))] = distance
except KeyboardInterrupt:
    print('Stopping.')
lidar.stop()
lidar.disconnect()



