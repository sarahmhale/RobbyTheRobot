import unittest

from Position import createPosition

class PositionTest(unittest.TestCase):
    def test_createPosition(self):
        pos = createPosition(x=2, y=4)
        
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 4)
        print (pos)
        print ("x: {}, y: {}".format(pos.x, pos.y))

if __name__ == '__main__':
    unittest.main()
