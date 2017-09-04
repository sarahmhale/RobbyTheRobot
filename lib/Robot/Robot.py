from Calculations.Angle import Angle
class Robot:

    currentPosition = 0
    destinationPosition = 0
    path = 0

    def turnRobot(self,destinationPosition, currentPosition, currentDestinationPos):
        angle=Angle()
        currentBearing = angle.vector(currentDestinationPosition, currentPosition)
        destinationBearing = angle.vector(destinationPosition,currentPosition)
        turnAngle = angle.angleBetweenVectors(currentBearing, destinationBearing)
        # TODO: Set wheel speed

    def currentPosition(self,position):
        self.currentPosition = position

    def destinationPosition(self, position):
        self.destinationPosition = position

    def getCurrentPosition(self):
        return self.currentPosition

    def getDestinationPosition(self):
        return self.destinationPosition = position

    def setPath(path):
        self.path = path
