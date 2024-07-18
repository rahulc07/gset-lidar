import numpy as np
import math
import rdp


def dp(segments):
    epsilon = 0.75
    for i in range(len(segments) - 1):
        simplified_points = rdp.rdp(segments[i], epsilon)
        print("Simplified Points:\n", simplified_points)


def calculate_gradient(points):
    gradients = []
    for i in range(len(points) - 1):
        dx = points[i + 1][0] - points[i][0]
        dy = points[i + 1][1] - points[i][1]
        gradient = dy / dx if dx != 0 else np.inf
        gradients.append(gradient)
    return gradients


def detect_potholes(segments, gradient_threshold=0.5):
    potholes = []
    simplified_segments = dp(segments)
    for segment in simplified_segments:
        gradients = calculate_gradient(segment)
        for i, gradient in enumerate(gradients):
            if i > 0 and abs(gradients[i] - gradients[i - 1]) > gradient_threshold:
                potholes.append(segment[i])
    return potholes
