import unittest

from math import sqrt
from Distance import Distance

class DistanceTest(unittest.TestCase):
    def test_shouldBeRightDistance(self):
        distance = Distance()
        list1 = [0,0]
        list2=[0,3]
        self.assertEqual(distance.getDistance(list1,list2), 3)
        list1 = [-2,-3]
        list2=[-4,4]
        self.assertEqual(distance.getDistance(list1,list2), sqrt(53))

    def test_ifPositionIsUndefinedReturnNone(self):
        distance = Distance()
        list1 = None
        list2=[0,3]
        self.assertEqual(distance.getDistance(list1,list2), None)

if __name__ == '__main__':
    unittest.main()
