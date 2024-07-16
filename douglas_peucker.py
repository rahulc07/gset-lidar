import numpy as np
import math
import rdp
points = np.array([
    [0, 0],
    [1, 0.1],
    [2, -0.1],
    [3, 5],
    [4, 6],
    [5, 7],
    [6, 8.1],
    [7, 9],
    [8, 9.1],
    [9, 9.2]
])

epsilon = 0.75
simplified_points = rdp.rdp(points, epsilon)


print("Original Points:\n", points)
print("Simplified Points:\n", simplified_points)
