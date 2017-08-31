from collections import namedtuple

def createPosition(x, y):
    Position = namedtuple('Position', ['x', 'y'])
    p = Position(x=x, y=y)
    return p
