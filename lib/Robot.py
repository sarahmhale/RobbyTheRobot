from lib.Angle.Angle import Angle
from lib.Speed.Speed import Speed
from lib.Position.Position import Position
from lib.Distance.Distance import Distance
class Robot:

    currentPosition = 0
    destinationPosition = 0
    path = 0

    def turn(self):
        currentPosition = Position().getPose()
        print('currentPosition',currentPosition)
        destinationPositions = Distance().getCordinatesWithinMaxDistance(currentPosition, 1, self.path)
        #angle = Angle()
        #speed = Speed()

        #currentBearing = angle.vector(self.destinationPosition, currentPosition)
        #destinationBearing = angle.vector(destinationPosition,currentPosition)
        #turnAngle = angle.angleBetweenVectors(currentBearing, destinationBearing)
        
        #speed.wheelSpeed(turnAngle, 0.5)

    def currentPosition(self,position):
        self.currentPosition = position

    def setDestinationPosition(self, position):
        self.destinationPosition = position

    def getCurrentPosition(self):
        return self.currentPosition

    def getDestinationPosition(self):
        return self.destinationPosition

    def setPath(self,path):
        self.path = path
       
