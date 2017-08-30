# coding=utf-8
from math import sqrt, fabs, pow
class Distance:
	"""
	Function name: getDistance
	Purpose: get distance between two coordinates
	Input: [x,y] , [x,y]
	Output: distance between the coordinates as a double
	Comments: används av getCordinatesWithinRange
	"""
	def getDistance(self,currentCoordinates, pathCoordinates):
		if(currentCoordinates == None or pathCoordinates == None):
			return None
		return sqrt(pow(fabs(currentCoordinates[0]-pathCoordinates[0]), 2)+pow(fabs(currentCoordinates[1]-pathCoordinates[1]),2))


"""
Function name: getCordinatesWithinRange
Purpose:
Input: path, rangeValue
Output: a list of all cordinates within range sorted by furthest distance first.
Comments:
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
