import numpy as np
import math
import rdp
def dp(segments):
    epsilon = 0.75
    for i in range(len(segments) -1):
        simplified_points = rdp.rdp(segments[i], epsilon)
        print("Simplified Points:\n", simplified_points)
