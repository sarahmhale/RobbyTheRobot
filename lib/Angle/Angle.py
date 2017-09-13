import math
class Angle:
    def vector(self,firstCoordinate, secondCoordinate):
        return ([firstCoordinate.x - secondCoordinate.x,  firstCoordinate.y -secondCoordinate.y])

    def angleBetweenVectors(self,v1, v2):
        
        v1_theta = math.atan2(v1[1], v1[0])
        v2_theta = math.atan2(v2[1], v2[0])        

        angle = (v2_theta - v1_theta) * (180.0 / math.pi)
        
        print(angle)

        if angle > 180:
            return angle - 360
        else:
            return angle
