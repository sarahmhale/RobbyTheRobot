import json, time
from lib.Position.Position import Position
from lib.Robot import Robot


def readPathFromJSONFile():
    with open('Path-around-bench-and-sofa.json') as data_file:
        data = json.load(data_file)
        path = []
        for row in data:
            path.append(row)       
    return path



if __name__ == '__main__':
    robot = Robot()
    robot.setPath(readPathFromJSONFile())
    
    i = 0
    while not (robot.reachedGoal()):
        robot.turn()
        time.sleep(0.1)
    
    print('GOAL')
    
 
