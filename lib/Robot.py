from lib.Angle.Angle import Angle
from lib.Speed.Speed import Speed
from lib.Position.Position import Position
from lib.Distance.Distance import Distance
class Robot:
    currentPosition = 0
    destinationPosition = 0
    path = 0
    index = 0

    def turn(self):
        currentPosition = Position().getPose()
        print('self path before' , self.path)
        destinationPosition, self.index = Distance().getCordinatesWithinMaxDistance(self.index,currentPosition, 0.5, self.path)

        if len(destinationPosition) != 0 :  
            turnAngle = self.calculateAngle(destinationPosition[0], currentPosition)
            self.destinationPosition = destinationPosition[0]
        else:  
            turnAngle = self.calculateAngle(self.destinationPosition, currentPosition)
        
        print('turnAngle',turnAngle)  
        Speed().wheelSpeed(turnAngle, 0.1)
       
    def calculateAngle(self,destinationPosition, currentPosition):
        print('Desitination to go:', destinationPosition)
        currentBearing = Angle().getHeading(currentPosition)
        destinationBearing = Angle().getBearingTo(destinationPosition['Pose']['Position'])
        print('current',currentBearing)
        print('destination',destinationBearing)
        
        return Angle().angleDifference(currentBearing, destinationBearing)
                
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
       
