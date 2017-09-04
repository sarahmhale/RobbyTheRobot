MRDS_URL = 'localhost:50000'

import http.client, json, time
from collections import namedtuple

HEADERS = {"Content-type": "application/json", "Accept": "text/json"}
class Position:
    def createPosition(x, y):
        Position = namedtuple('Position', ['x', 'y'])
        p = Position(x=x, y=y)
        return p

    """
    Author: Erik Billing (billing@cs.umu.se)

    Updated by Ola Ringdahl 204-09-11
    Updated by Lennart Jern 20016-09-06 (converted to Python 3)
    """
    def getPose():
        """Reads the current position and orientation from the MRDS"""
        mrds = http.client.HTTPConnection(MRDS_URL)
        mrds.request('GET','/lokarria/localization')
        response = mrds.getresponse()
        if (response.status == 200):
            poseData = response.read()
            response.close()
            return json.loads(poseData.decode())
        else:
            return UnexpectedResponse(response)

    """
    Author: Erik Billing (billing@cs.umu.se)

    Updated by Ola Ringdahl 204-09-11
    Updated by Lennart Jern 20016-09-06 (converted to Python 3)
    """
    def postSpeed(angularSpeed,linearSpeed):
        """Sends a speed command to the MRDS server"""
        mrds = http.client.HTTPConnection(MRDS_URL)
        params = json.dumps({'TargetAngularSpeed':angularSpeed,'TargetLinearSpeed':linearSpeed})
        mrds.request('POST','/lokarria/differentialdrive',params,HEADERS)
        response = mrds.getresponse()
        status = response.status
        #response.close()
        if status == 204:
            return response
        else:
            raise UnexpectedResponse(response)
