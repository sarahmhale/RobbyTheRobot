MRDS_URL = 'localhost:50000'

import http.client, json, time
from collections import namedtuple
import math

HEADERS = {"Content-type": "application/json", "Accept": "text/json"}
class Speed:
    def postSpeed(self,angularSpeed, linnearSpeed):
        """Sends a speed command to the MRDS server"""
        mrds = http.client.HTTPConnection(MRDS_URL)
        params = json.dumps({'TargetAngularSpeed':angularSpeed,'TargetLinearSpeed': linnearSpeed})
        mrds.request('POST','/lokarria/differentialdrive',params,HEADERS)
        response = mrds.getresponse()
        status = response.status
        response.close()
        if status == 204:
            return response
        else:   
            raise UnexpectedResponse(response)
        

    
        
