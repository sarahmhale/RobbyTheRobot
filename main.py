import json
from lib.Position.Position import Position
from pprint import pprint

def readPathFromJSONFile:
    with open('Path-around-bench-and-sofa.json') as data_file:
        data = json.load(data_file)
        path = []
        for index in data:
            path.append(Position.createPosition(x=index['Pose']['Position']['X'],y=index['Pose']['Position']['Y']))

    return path

# 
# main:
#
#     Robot.setPath(readPathFromJSONFile)
