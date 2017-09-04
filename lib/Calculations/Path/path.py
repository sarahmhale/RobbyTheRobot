import json
from collections import namedtuple

from pprint import pprint
import unittest

class Path:
    def __init__(self, file):
        self._file = file
        
        
    def import_path(self):
        with open('self.file') as data_file:
            data = json.load(data_file)
            
        pprint(data)
                
        
    
    
    
    
def createPos(x, y):
    coordinate = coordinateNamedTuple("x"=x, "y"=y)
    return coordinate













class TestPathMethods(unittest.TestCase):
    
    def test_init(self):
        p = Path()
        coordinate = createPos
            
    

if __name__ == '__main__':
    unittest.main()
