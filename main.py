import json
from lib.Position.Position import Position
from pprint import pprint

def readPathFromJSONFile:
    with open('Path-around-bench-and-sofa.json') as data_file:
        data = json.load(data_file)
        path = []
        for row in data:
            x = row['Pose']['Position']['X']
            y = row['Pose']['Position']['Y']
            path.append(Position.createPosition(x = x, y = y))

    return path

#
# main:
# Robot.setPath(readPathFromJSONFile)
#
#   while(!reachedGoal()):
#       move()
#       timeout( millisek)
#
#  def move():
#
#     postionList = pieceOfThePath(distanceToObstacle())
#      turnRobot( postionList[0], Robot.getCurrentPosition(), Robot.getCurrentDestinationPosition())

#
