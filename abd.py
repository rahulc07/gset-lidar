import numpy
# This is an Adaptive Breakpoint Detection Algorithm based on 
# https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7993890
# and https://publications.lib.chalmers.se/records/fulltext/253622/253622.pdf
# Threshold init 
dmax = 0
# This is the worst case incidence angle for the sensor (AKA the angle of the lidar sensor with the surface)
lamb = 45
# Inital values
standard_deviation = 1
distances = []
angles = []
segments = []
# Final equation

# This should be run after the point cloud is generated
def abd(point_cloud):
    segments = []
    for point in point_cloud:
        distances.append(point[1])
    global standard_deviation
    #standard_deviation = numpy.std(distances)
    print(standard_deviation)
    current_segment = 0
    # Put the very first value into segments
    segments.append([])
    segments[0].append(point_cloud[0])
    for i in range(len(point_cloud) - 1):
        dmax = calc_dmax(point_cloud[i], point_cloud[i+1])
        distance_between_points = numpy.sqrt(((point_cloud[i+1][0] - point_cloud[i][0]) ** 2) + ((point_cloud[i+1][1] - point_cloud[i][1]) **2))
        if distance_between_points > dmax:
            current_segment += 1
            segments.append([])
        segments[current_segment].append(point_cloud[i+1])
    return segments

def calc_dmax(point1, point2):
    angle_difference = point2[1] - point1[1]
    # Page 32/96 of the second paper
    dmax = point1[0] * (numpy.sin(angle_difference)/numpy.sin(lamb - angle_difference)) + (3 * standard_deviation)
    return dmax



    


