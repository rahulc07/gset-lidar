import numpy
# This is an Adaptive Breakpoint Detection Algorithm based on 
# https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7993890
# and https://publications.lib.chalmers.se/records/fulltext/253622/253622.pdf
# Threshold init 
dmax = 0
# This is the worst case incidence angle for the sensor (AKA the angle with the surface)
lamb = 16
# Inital values
standard_deviation = 1
distances = []
angles = []
segments = []
# Final equation

# This should be run after the point cloud is generated
def abd(point_cloud):
    for point in point_cloud:
        distances.append(point[1])
    standard_deviation = numpy.std(distances)
    current_segment = 0
    # Put the very first value into segments
    segment[0] = point_cloud[0]
    for i in range(len(point_cloud) - 1):
        dmax = calc_dmax(point_cloud[i], point_cloud[i+1])
        distance_between_points = sqrt(((point_cloud[i+1][0] - point_cloud[i][0]) ** 2) + ((point_cloud[i+1][1] - point_cloud[i][1]) **2))
        if distance_between_points > dmax:
            current_segment += 1
        segments[current_segment].append(point_cloud[i+1])

def calc_dmax(point1, point2):
    angle_difference = point2[1] - point1[1]
    # Page 32/96 of the second paper
    dmax = point1[0] * (numpy.sin(angle_difference)/numpy.sin(lamb - angle_difference)) + (3 * standard_deviation)
    return dmax



    

