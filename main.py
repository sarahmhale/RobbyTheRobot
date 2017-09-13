import json, time
from lib.Position.Position import Position
from lib.Robot import Robot
def readPathFromJSONFile():
    with open('Path-around-bench-and-sofa.json') as data_file:
        data = json.load(data_file)
        path = []
        for row in data:
            x = row['Pose']['Position']['X']
            y = row['Pose']['Position']['Y']
            path.append(Position.createPosition(x = x, y = y))

    return path



if __name__ == '__main__':
    robot = Robot()
    pose = Position()
    robot.turn(pose.getPose())
    time.sleep(3)
   

#
# main:
# Robot.setPath(readPathFromJSONFile)
#
#   while(!reachedGoal()):
#       move()
#       timeout( millisek)
#
#  def move():
#     postionList = pieceOfThePath(distanceToObstacle())
#     turnRobot( postionList[0], Position.getPose())
#
