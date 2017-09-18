import math
class Angle:
    def heading(self,q):
        return self.rotate(q,{'X':1.0,'Y':0.0,"Z":0.0})    
    
    def rotate(self,q,v):
        return self.vector(self.qmult(self.qmult(q,self.quaternion(v)),self.conjugate(q)))
    
    def quaternion(self,v):
        q=v.copy()
        q['W']=0.0;
        return q
    
    def vector(self,q):
        v={}
        v["X"]=q["X"]
        v["Y"]=q["Y"]
        v["Z"]=q["Z"]
        return v
    
    def conjugate(self,q):
        qc=q.copy()
        qc["X"]=-q["X"]
        qc["Y"]=-q["Y"]
        qc["Z"]=-q["Z"]
        return qc
    
    def qmult(self,q1,q2):
        q={}
        q["W"]=q1["W"]*q2["W"]-q1["X"]*q2["X"]-q1["Y"]*q2["Y"]-q1["Z"]*q2["Z"]
        q["X"]=q1["W"]*q2["X"]+q1["X"]*q2["W"]+q1["Y"]*q2["Z"]-q1["Z"]*q2["Y"]
        q["Y"]=q1["W"]*q2["Y"]-q1["X"]*q2["Z"]+q1["Y"]*q2["W"]+q1["Z"]*q2["X"]
        q["Z"]=q1["W"]*q2["Z"]+q1["X"]*q2["Y"]-q1["Y"]*q2["X"]+q1["Z"]*q2["W"]
        return q
        
    def getHeading(self,pose):
        """Returns the XY Orientation as a heading unit vector"""
        vector = self.heading(pose['Pose']['Orientation'])
        return math.atan2( vector['Y'], vector['X'])   
    
    def getBearingTo(self,destinationPosition,currentPosition):
        return math.atan2( destinationPosition['Y'] - currentPosition['Y'],destinationPosition['X']- currentPosition['X'])
        
    def angleDifference(self,headingAngle, destinationAngle):
        error = destinationAngle - headingAngle
        if(error > math.pi):
            return error - math.pi*2
        elif(error < - math.pi):
            return error+math.pi*2
        elif(error == 0):
            return 0
        else:
            return error
    
        