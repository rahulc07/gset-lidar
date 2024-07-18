import scipy

def convex_hull_volume(three_d_point_cloud):
    hull = scipy.spatial.ConvexHull(three_d_point_cloud)
    volume = hull.volume
    return volume
