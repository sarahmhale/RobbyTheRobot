from lib.Angle.Angle import Angle
from lib.Position.Position import Position
class Robot:

    currentPosition = 0
    destinationPosition = 0
    path = 0

    def turn(self,destinationPosition):
        position = Position()
        angle=Angle()
        currentPosition = position.getPose()
        currentBearing = angle.vector(self.destinationPosition, currentPosition)
        destinationBearing = angle.vector(destinationPosition,currentPosition)
        turnAngle = angle.angleBetweenVectors(currentBearing, destinationBearing)
        # TODO: Set wheel speed

    def currentPosition(self,position):
        self.currentPosition = position

    def setDestinationPosition(self, position):
        self.destinationPosition = position

    def getCurrentPosition(self):
        return self.currentPosition

    def getDestinationPosition(self):
        return self.destinationPosition

    def setPath(path):
        self.path = path
