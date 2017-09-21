import json, time
from lib.Position.Position import Position
from lib.Timer.Timer import Timer
from lib.Robot import Robot


def readPathFromJSONFile():
    with open('Path-around-table-and-back.json') as data_file:
        data = json.load(data_file)
        path = []
        for row in data:
            path.append(row)       
    return path



if __name__ == '__main__':
    robot = Robot()
    timer = Timer()
    robot.setPath(readPathFromJSONFile())
    
    timer.startTimer()
    while not (robot.reachedGoal()):
        robot.turn()
        time.sleep(0.1)
    
    timer.stopTimer()
    
 
