MRDS_URL = 'localhost:50000'

import http.client, json, time
from collections import namedtuple
import math

HEADERS = {"Content-type": "application/json", "Accept": "text/json"}
class Speed:
    """
    Author: Erik Billing (billing@cs.umu.se)

    Updated by Ola Ringdahl 204-09-11
    Updated by Lennart Jern 20016-09-06 (converted to Python 3)
    """
    def postSpeed(self,angularSpeed):
        """Sends a speed command to the MRDS server"""
        mrds = http.client.HTTPConnection(MRDS_URL)
        params = json.dumps({'TargetAngularSpeed':angularSpeed,'TargetLinearSpeed': 1})
        mrds.request('POST','/lokarria/differentialdrive',params,HEADERS)
        response = mrds.getresponse()
        status = response.status
        response.close()
        if status == 204:
            return response
        else:   
            raise UnexpectedResponse(response)
        
    def wheelSpeed(self,angle, time):
        self.postSpeed(angle /time)
        
