# coding=utf-8
import numpy as np

class Angle:

    def getAngle(self,currentVector, currentCoordinate, destinationCoordinate):
        v1 = [currentVector['x'], currentVector['y']]
        v2 = [destinationCoordinate['x'] - currentCoordinate['x'],  destinationCoordinate['y'] -currentCoordinate['y']]
        ang1 = np.arctan2(*v1[::-1])
        ang2 = np.arctan2(*v2[::-1])
        return np.rad2deg((ang1 - ang2) % (2 * np.pi))


"""
Function name:
Purpose:
Input:
Output:
Comments:
"""
