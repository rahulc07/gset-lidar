# %%
from time import sleep
import scipy
import numpy as np
import matplotlib.pyplot as plt


def convex_hull_volume(three_d_point_cloud):
    hull = scipy.spatial.ConvexHull(three_d_point_cloud)
    volume = hull.volume
    print(volume)
    plot_convex_hull(hull)


def plot_convex_hull(hull):

    points = hull.points

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plot defining corner points
    ax.plot(points.T[0], points.T[1], points.T[2], "ko")

    # 12 = 2 * 6 faces are the simplices (2 simplices per square face)
    for simplex in hull.simplices:
        # Here we cycle back to the first coordinate
        simplex = np.append(simplex, simplex[0])
        ax.plot(points[simplex, 0], points[simplex, 1],
                points[simplex, 2], "r-")

    # Make axis label
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()

def plot_3d_point_cloud(points):
    if not all(len(point) == 3 for point in points):
        raise ValueError("All points must have 3 coordinates (x, y, z)")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    xs, ys, zs = zip(*points)
    
    ax.scatter(xs, ys, zs)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Point Cloud')
    
    plt.show()


def plot_point_cloud(points):
    points = np.array(points)  # Convert the list to a NumPy array for plotting

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plot the entire point cloud
    ax.scatter(points.T[0], points.T[1], points.T[2],
               c="blue", marker="o", alpha=0.5)

    # Set axis labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()
