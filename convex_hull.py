from time import sleep
import scipy
import numpy as np
import matplotlib.pyplot as plt
def convex_hull_volume(three_d_point_cloud):
    hull = scipy.spatial.ConvexHull(three_d_point_cloud)
    volume = hull.volume
    convex_hull_plot(hull, three_d_point_cloud)
def convex_hull_plot(hull, pts):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plot defining corner points
    ax.plot(pts.T[0], pts.T[1], pts.T[2], "ko")

    # 12 = 2 * 6 faces are the simplices (2 simplices per square face)
    for s in hull.simplices:
        s = np.append(s, s[0])  # Here we cycle back to the first coordinate
        ax.plot(pts[s, 0], pts[s, 1], pts[s, 2], "r-")

    # Make axis label
    for i in ["x", "y", "z"]:
        eval("ax.set_{:s}label('{:s}')".format(i, i))

    plt.show()
