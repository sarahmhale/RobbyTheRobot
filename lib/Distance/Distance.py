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
		return sqrt(pow(fabs(currentCoordinates.x-pathCoordinates.x), 2)+pow(fabs(currentCoordinates.y-pathCoordinates.y),2))



	"""
	Function name: getCordinatesWithinMaxDistance
	Purpose:
	Input: path, rangeValue
	Output: a list of all cordinates within range sorted by furthest distance first.
	Comments:
	"""

	def getCordinatesWithinMaxDistance(self,robotCoordinate, maxLookAheadRange, path):
		coordinatesWithinMaxDistance = []
		for coordinate in path:
			distance = self.getDistance(robotCoordinate, coordinate)
			print(distance)
			if(distance <= maxLookAheadRange):
				coordinatesWithinMaxDistance.insert(0,distance)
			else:
				break
		print(coordinatesWithinMaxDistance)
		return coordinatesWithinMaxDistance



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
