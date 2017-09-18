# coding=utf-8
from math import sqrt, fabs, pow


class Distance:
	def getDistance(self,currentCoordinates, pathCoordinates):
		return sqrt(pow(currentCoordinates['X']-pathCoordinates['X'], 2)+pow(currentCoordinates['Y']-pathCoordinates['Y'],2))


	def getCordinatesWithinMaxDistance(self,index,robotCoordinate, maxLookAheadRange,path):
		coordinatesWithinMaxDistance = []
		while index < len(path):
			distance = self.getDistance(robotCoordinate['Pose']['Position'], path[index]['Pose']['Position'])
			if(distance <= maxLookAheadRange):
				coordinatesWithinMaxDistance.insert(0, path[index])
				index = index + 1
			else:
				break
		return coordinatesWithinMaxDistance, index

