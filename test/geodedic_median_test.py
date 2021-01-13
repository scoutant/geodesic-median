import unittest
from geodesic_median import geodist
from geodesic_median import geodesic_median
from geodesic_median import weighted_geodesic_median
from scipy.spatial.distance import euclidean
import geopy.distance

eps = 0.001
central_park=[40.785091,-73.968285]
statue_of_liberty=[40.688930,-74.044100]
empire_state_building=[40.748817,-73.985428]
brooklyn_bridge=[40.7058094,-73.9981622]

class GeodesicMedianTest(unittest.TestCase):

    def test_distance(self):
        d = geopy.distance.distance(central_park, statue_of_liberty).km # defaulting to geodesic distance
        print(d)
        self.assertTrue(12<d<13)

    def test_geodist(self):
        X = [statue_of_liberty, empire_state_building, brooklyn_bridge ]
        Y = [central_park ]
        D = geodist(X,Y)
        self.assertTrue( D.shape==(3,1))
        self.assertTrue(12<D[0]<13)

    def test_4_poi(self):
        X = [central_park, statue_of_liberty, empire_state_building, brooklyn_bridge ]
        m = geodesic_median(X, eps)
        self.assertTrue(euclidean(m, [40.73269615, -73.99497747])<eps ) # near 5th ave / E 9th s

    def test_4_weighted_poi(self):
        X = [central_park, statue_of_liberty, empire_state_building, brooklyn_bridge]
        m = weighted_geodesic_median(X, [1, 2, 1, 1], eps)
        self.assertTrue(euclidean(m, [40.71154659, -74.00746579]) < 2*eps)  # city hall park