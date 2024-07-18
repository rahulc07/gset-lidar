import numpy as np
import math
import rdp

gradient_threshold = .75
episolon = .75
def dp(segments):
    print(len(segments))
    new_segs = []
    for i in range(len(segments)):
        simp = rdp.rdp(segments[i], episolon)
        new_segs.append(simp)
    print(new_segs)
    return new_segs
    




def clean_data(segments):
    for i in range (len(segments) -1):
        if len(segments[i]) < 2:
            segments.pop(i)
    return segments


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
    


