import numpy as np
import math
import rdp

gradient_threshold = .75

def dp(segments):
    epsilon = 0.75
    for i in range(len(segments) - 1):
        simplified_points = rdp.rdp(segments[i], epsilon)
        #print("Simplified Points:\n", simplified_points)
        return simplified_points

def clean_data(segments):
    for i in range (len(segments) -1):
        if len(segments[i]) > 2:
            segments.pop(i)


def calculate_slope(segment):
    for point in range(1,len(segment)-1):
         slope =  (segment[point][1] - segment[point-1][1])/(segment[point][0] - segment[point-1][0])
         return slope

def check_pothole(simplified_segments):
    clean = clean_data(simplified_segments)
    for segment in range(1, len(clean)-1):
        diff = np.abs(calculate_slope(clean[segment]) - calculate_slope(clean[segment-1]))
        if diff >= gradient_threshold:
            print("POTHOLE")
    


