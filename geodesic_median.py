import numpy as np
from scipy.spatial.distance import cdist, euclidean
import geopy.distance

def geodist(X,Y):
    """ mimicking scipy cdist : computing all the distances for all the pair of the two collections of inputs. But using geodesic distance """
    D = np.ndarray( (len(X), len(Y)) )
    for i in range(0, len(X)):
        for j in range(0, 1):
            D[i,j] = geopy.distance.distance( X[i], Y[j]).km
    return D

def geodesic_median(X, eps=1e-6):
    """
    Computes geometric median
    :param X: the list of sample points using (latitude,longitude) coordinate system. In degrees, not radian.
    :param eps: acceptable error margin
    :return: first estimate meeting eps
    """
    y = np.mean(X,0) # the geometric mean is a fare start
    while True:
        while np.any(cdist(X,[y])==0): # no matter the distance definition used, we just need to filter out null distances
            y +=0.1*np.ones(len(y))
        # set of weights that are the inverse of the distances from current estimate to the observations
        W = 1/geodist(X,[y]) # element-wise
        # new estimate is the weighted average of the sample points
        y1 = np.sum(W*X,0)/np.sum(W) # sum along axis 0
        if euclidean(y,y1) < eps: # euclidean distance is enough for the test
            return y1
        y = y1


def weighted_geodesic_median(X, WX, eps=1e-6):
    """
    Computes weighted geometric median
    :param X: the list of sample points using (latitude,longitude) coordinate system. In degrees, not radian.
    :param WX: the list of weights
    :param eps: acceptable error margin
    :return: first estimate meeting eps
    """
    y = np.average(X,axis=0,weights=WX)
    while True:
        while np.any(cdist(X,[y])==0):
            y +=0.1*np.ones(len(y))
        W = np.expand_dims(WX,axis=1)/geodist(X,[y]) # element-wise operation
        y1 = np.sum(W*X,0)/np.sum(W)
        if euclidean(y,y1) < eps:
            return y1
        y = y1