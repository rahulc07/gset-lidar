import abd
import numpy as np

# Convert the 2D Point Cloud to 3D to make a convex hull

# x is forward and backwards FROM THE SENSOR
# y is left and right
# z is depth

def convert_to_3d(point_cloud):
    three_dimensional_point_cloud = []
    for point in point_cloud:
        rotation_angle = point[0]
        distance = point[1]
        # If this math works I am him - Rahul
        y = distance * np.cos(abd.lamb) * np.cos(rotation_angle)
        x = distance * np.cos(abd.lamb) * np.sin(rotation_angle)
        z = distance * np.sin(abd.lamb)
        three_dimensional_point_cloud.append([x, y, z])
        return three_dimensional_point_cloud
