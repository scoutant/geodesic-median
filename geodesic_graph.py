import numpy as np
import matplotlib.pyplot as plt
from geodesic_median import geodesic_median
import geopy.distance

"""
Geodesic median 3D display. 
"""

points = np.array([ # lat,lng in degrees
    [20, 0],
    [0, -20],
    [0, 20],
])
size=60

def minisum(X,y):
    """ sum of geodesic distances in km """
    d = 0
    for t in X:
        d += geopy.distance.distance(y, t).km
    return d


if __name__ == '__main__':
    ax = plt.axes(projection='3d')

    x = np.linspace(-90, 90, size)
    y = np.linspace(-180, 180, size)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros( (size,size))

    for i in range(size):
        for j in range(size):
            Z[j][i] = minisum( points, [X[0][i], Y[j][0]])

    fig = plt.figure(1, figsize=(100, 100), dpi=300)

    ax.contour3D(X, Y, Z, size, cmap='binary')

    n = geodesic_median(points)
    print(f"geometric median n : {n}")
    ax.scatter3D( [n[0]], [n[1]], [minisum(points,n)], cmap = 'Reds')

    ax.view_init(20, -85) # initialize point of view

    plt.show()
