#abd.py
import numpy
# This is an Adaptive Breakpoint Detection Algorithm based on 
# https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7993890
# and https://publications.lib.chalmers.se/records/fulltext/253622/253622.pdf
# Threshold init 
dmax = 0
# This is the worst case incidence angle for the sensor (AKA the angle of the lidar sensor with the surface)
lamb = 45
# Inital values
distances = []
angles = []
segments = []
# Final equation

# This should be run after the point cloud is generated
def abd(point_cloud):
    distances = []
    segments = []
    
    for point in point_cloud:
        distances.append(point[1])
    standard_deviation = numpy.std(distances)
    #standard_deviation = 1
    #print(standard_deviation)
    current_segment = 0
    # Put the very first value into segments
    segments.append([])
    segments[0].append(point_cloud[0])
    for i in range(len(point_cloud) - 1):
        dmax = calc_dmax(point_cloud[i], point_cloud[i+1], standard_deviation)
        distance_between_points = numpy.sqrt(((point_cloud[i+1][0] - point_cloud[i][0]) ** 2) + ((point_cloud[i+1][1] - point_cloud[i][1]) **2))
        if distance_between_points > dmax:
            if len(segments[current_segment]) < 2:
                segments.pop(current_segment)
                current_segment -= 1
            current_segment += 1
            segments.append([])
        segments[current_segment].append(point_cloud[i+1])
    #print(len(segments))
    return segments

def calc_dmax(point1, point2, standard_deviation):
    angle_difference = point2[0] - point1[0]
    # Page 32/96 of the second paper
    angle_difference_rads = angle_difference * .0174
    lamb_rads = lamb * .0174
    dmax = (point1[1] * numpy.sin(angle_difference_rads))/(numpy.sin(lamb_rads - angle_difference_rads)) + (3 * standard_deviation)
    #print(dmax)
    return dmax



    


