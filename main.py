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
            path.append(Position().createPosition(x = x, y = y))
    print('path: ' , path)        
    return path



if __name__ == '__main__':
    robot = Robot()
    robot.setPath(readPathFromJSONFile())
   
    robot.turn()
    
    
 
