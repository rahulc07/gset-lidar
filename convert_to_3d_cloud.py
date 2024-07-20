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
        lamb_radians = abd.lamb * .0174
        x = float(distance * np.cos(abd.lamb) * np.cos(rotation_angle))
        y = float(distance * np.cos(abd.lamb) * np.sin(rotation_angle))
        z = float(distance * np.sin(abd.lamb))
        three_dimensional_point_cloud.append([x, y, z])
    print(three_dimensional_point_cloud)
    z_min = find_z_min(three_dimensional_point_cloud)
    new_three_dimensional_point_cloud  = []
    for i in range(len(three_dimensional_point_cloud)):
         #if (three_dimensional_point_cloud[i][2] - z_min) > 3:
        three_dimensional_point_cloud[i][2] -=254
        new_three_dimensional_point_cloud.append(three_dimensional_point_cloud[i])
    return new_three_dimensional_point_cloud 

def find_z_min(three_dimensional_point_cloud):
    current_min = 10000
    for point in three_dimensional_point_cloud:
        if point[2] < current_min:
            current_min = point[2]
    return current_min

