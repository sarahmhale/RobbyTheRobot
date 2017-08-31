from collections import namedTuple





"""
Function name: getCordinatesWithinMaxDistance
Purpose:
Input: path, rangeValue
Output: a list of all cordinates within range sorted by furthest distance first.
Comments:
"""

def getCordinatesWithinMaxDistance(robotCoordinate, goalCoordinate, maxDistanceFromPath):
	coordinatesWithinMaxDistanceDic = {}
	for (coordinate in path):
		distance = getDistance(robotCoordinate, coordinate)
		if(distance <= maxDistanceFromPath):
			coordinatesWithinMaxDistanceDic[coordinate] = distance
		else:
			break
	return coordinatesWithinMaxDistanceDic




cordinate = [x, y]

list cordinatesWithinRange
bool inRange = true
int index
while(inRange):
	
	 if getDistance(path[index]) <= rangeValue
		cordinatesWithinRange.append.[cordinate, length]
		cordinatesWithinRange.sort(1)
		
return sortByLength(cordinatesWithinRange)














"""
Function name: getDistance
Purpose: get distance between two coordinates
Input: [x,y] , [x,y]
Output: distance between the coordinates as a double
Comments: används av getCordinatesWithinRange
"""

"""
Function name:
Purpose:
Input:
Output:
Comments: används av getCordinatesWithinRange
"""

"""
Function name:
Purpose:
Input:
Output:
Comments:
"""