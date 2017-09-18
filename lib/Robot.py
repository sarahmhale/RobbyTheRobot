from lib.Angle.Angle import Angle
from lib.Speed.Speed import Speed
from lib.Position.Position import Position
from lib.Distance.Distance import Distance
class Robot:
    destinationPosition = 0
    path = 0
    index = 0
    goalIndex = 0

    def turn(self):
        currentPosition = Position().getPose()
        destinationPosition, self.index = Distance().getCordinatesWithinMaxDistance(self.index,currentPosition, 1, self.path)


        if len(destinationPosition) != 0 :  
            turnAngle = self.calculateAngle(destinationPosition[0], currentPosition)
            self.destinationPosition = destinationPosition[0]
        else:  
            turnAngle = self.calculateAngle(self.destinationPosition, currentPosition)

        Speed().postSpeed(turnAngle)
       
    def calculateAngle(self,destinationPosition, currentPosition):
        currentBearing = Angle().getHeading(currentPosition)
        destinationBearing = Angle().getBearingTo(
            destinationPosition['Pose']['Position'],
            currentPosition['Pose']['Position'])
        return Angle().angleDifference(currentBearing, destinationBearing)

    def setPath(self,path):
        self.path = path
        self.goalIndex = len(path)
        
    def reachedGoal(self):
        return self.index == self.goalIndex
       
