# %%
from time import sleep
import scipy
import numpy as np
import matplotlib.pyplot as plt
def convex_hull_volume(three_d_point_cloud):
    hull = scipy.spatial.ConvexHull(three_d_point_cloud)
    volume = hull.volume
    plot_convex_hull(hull)
def plot_convex_hull(hull):
    """
    Plots a convex hull object.

    Parameters:
    hull (scipy.spatial.ConvexHull): The convex hull object to plot.

    """
    if not isinstance(hull, scipy.spatial.ConvexHull):
        raise ValueError("The input must be a scipy.spatial.ConvexHull object")

    plt.figure()
    plt.plot(hull.points[:, 0], hull.points[:, 1], 'o', markersize=5, label='Points')
    
    for simplex in hull.simplices:
        plt.plot(hull.points[simplex, 0], hull.points[simplex, 1], 'k-')

    plt.plot(hull.points[hull.vertices, 0], hull.points[hull.vertices, 1], 'r--', lw=2, label='Convex Hull')
    plt.fill(hull.points[hull.vertices, 0], hull.points[hull.vertices, 1], 'c', alpha=0.3)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Convex Hull')
    plt.legend()
    plt.show()