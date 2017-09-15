# coding=utf-8
from math import sqrt, fabs, pow


class Distance:
	counter = 0
	"""
	Function name: getDistance
	Purpose: get distance between two coordinates
	Input: [x,y] , [x,y]
	Output: distance between the coordinates as a double
	Comments: används av getCordinatesWithinRange
	"""
	def getDistance(self,currentCoordinates, pathCoordinates):
		
		print('currentCoordinates  ',currentCoordinates)
		print('pathCoordinates ',pathCoordinates)
		if(currentCoordinates == None or pathCoordinates == None):
			return None
		return sqrt(pow(currentCoordinates['Pose']['Position']['X']-pathCoordinates['Pose']['Position']['X'], 2)+pow(currentCoordinates['Pose']['Position']['Y']-pathCoordinates['Pose']['Position']['Y'],2))



	"""
	Function name: getCordinatesWithinMaxDistance
	Purpose:
	Input: path, rangeValue
	Output: a list of all cordinates within range sorted by furthest distance first.
	Comments:
	"""

	def getCordinatesWithinMaxDistance(self,index,robotCoordinate, maxLookAheadRange,path):
		coordinatesWithinMaxDistance = []
		print('counter',index)
		while index < len(path):
			distance = self.getDistance(robotCoordinate, path[index])
			print('distance',distance)
			if(distance <= maxLookAheadRange):
				coordinatesWithinMaxDistance.insert(0, path[index])
				index = index + 1
			else:
				break
		print('path after ',path)
		return coordinatesWithinMaxDistance, index



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
