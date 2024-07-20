import abd
import numpy as np
import scipy.stats
# Convert the 2D Point Cloud to 3D to make a convex hull

# x is fleft right
# y is forward backward
# z is depth

def convert_to_3d(point_cloud):
    #print(point_cloud)
    three_dimensional_point_cloud = []
    for point in point_cloud:
        rotation_angle = point[0]
        distance = point[1]
        # If this math works I am him - Rahul
        lamb_radians = abd.lamb * .0174
        rotation_angle_rads = rotation_angle *.0174
        y = float(distance * np.cos(lamb_radians) * np.cos(rotation_angle_rads))
        # pi / 2 rads = 1.57
        if rotation_angle_rads > 3.14: 
            x = float(distance * np.cos(lamb_radians) * np.sin(6.28 - rotation_angle_rads))
        else:
            x = float(distance * np.cos(lamb_radians))
        z = float(distance * np.sin(lamb_radians))
        three_dimensional_point_cloud.append([x, y, z])
    #print(three_dimensional_point_cloud)
    z_min = find_z_min(three_dimensional_point_cloud)
    new_three_dimensional_point_cloud  = []
    # Get z mean
    z_array = []
    for point in three_dimensional_point_cloud:
        z_array.append(point[2])
    z_mean = np.median(z_array) 
    z_std = scipy.stats.iqr(z_array)

    for i in range(len(three_dimensional_point_cloud)):
        # Parameter tweak for volume anal
        # print(three_dimensional_point_cloud[i][2])
        if (three_dimensional_point_cloud[i][2] < z_mean + 2.5 * z_std) and (three_dimensional_point_cloud[i][2] > z_mean - 3 * z_std ):
        #if (three_dimensional_point_cloud[i][2] > np.percentile(z_array, 25) - 1.5 * z_std ) and (three_dimensional_point_cloud[i][2] < np.percentile(z_array, 75) + 1.5*z_std):
            #three_dimensional_point_cloud[i][2] -= z_min
            new_three_dimensional_point_cloud.append(three_dimensional_point_cloud[i])
    #print(new_three_dimensional_point_cloud)
    print(z_mean)
    print(z_std)
    return new_three_dimensional_point_cloud 

def find_z_min(three_dimensional_point_cloud):
    current_min = 10000
    for point in three_dimensional_point_cloud:
        if point[2] < current_min:
            current_min = point[2]
    return current_min

