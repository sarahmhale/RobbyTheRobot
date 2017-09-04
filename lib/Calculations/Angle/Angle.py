# coding=utf-8
import numpy as np

class Angle:
    def vector(firstCoordiante, secondCoordinate):
        return ([firstCoordinate.x - secondCoordinate.x,  firstCoordinate.y -secondCoordinate.y])

    def angleBetweenVectors(self,v1, v2):
        ang1 = np.arctan2(*v1[::-1])
        ang2 = np.arctan2(*v2[::-1])

        angle =np.rad2deg((ang1 - ang2) % (2 * np.pi))

        if angle > 180:
            return angle - 360
        else:
            return angle
