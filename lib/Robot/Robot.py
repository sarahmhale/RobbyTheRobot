from Calculations.Angle import Angle
class Robot:

    # currentPos

    def turnRobot(destinationPosition, currentPosition, currentDestinationPos):
        angle=Angle()
        currentBearing = angle.vector(currentDestinationPosition, currentPosition)
        destinationBearing = angle.vector(destinationPosition,currentPosition)
        turnAngle = angle.turnRobot(currentBearing, destinationBearing)
