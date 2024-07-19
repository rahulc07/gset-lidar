import numpy as np
import math
import rdp
# Each segment contains it's own point cloud
def dp(complex_segments):
    # Douglas Pecker Line Extraction
    simplified_segments = []
    for segment in complex_segments:
        simplified_segments.append(rdp.rdp(segment, epsilon=0.75))
    return simplified_segments
def calculate_slope(segment):
    return (segment[-1][1] - segment[0][1]) / (segment[-1][0] - segment[0][0])
def check_pothole(simplified_segments):
    print(simplified_segments)
    for segment in range(1, len(simplified_segments)-1):
        diff = np.abs(calculate_slope(simplified_segments[segment])) - np.abs(calculate_slope(simplified_segments[segment-1]))
        print(f'Difference: {diff}')
        if diff >= 1:
            print("Pothole")
            return True



    