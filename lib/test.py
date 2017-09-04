import unittest

from Position import Position
from Calculations.Angle import Angle

class AngleTest(unittest.TestCase):
    def test_shouldReturnVector(self):
        angle= Angle()
        pos1 = createPosition(x=3, y=4)
        pos2 = createPosition(x=3, y=5)

        pprint(angle.vector(pos1, pos2))
    def test_shouldReturn0degrees(self):
        angle = Angle()
        self.assertEqual(angle.getAngle({"x":0, "y":3}, {"x":0, "y":0}, {"x":0, "y":3}), 0)
    def test_shouldReturn90degrees(self):
        angle = Angle()
        self.assertEqual(angle.getAngle({"x":0, "y":1}, {"x":0, "y":0}, {"x":1, "y":0}), 90)
    def test_shouldReturnMinus90degrees(self):
        angle = Angle()
        self.assertEqual(angle.getAngle({"x":0, "y":1}, {"x":0, "y":0}, {"x":-1, "y":0}), -90)
if __name__ == '__main__':
    unittest.main()
