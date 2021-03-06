MRDS_URL = 'localhost:50000'

import http.client, json, time
from collections import namedtuple

HEADERS = {"Content-type": "application/json", "Accept": "text/json"}
class Position:
    """
    Author: Erik Billing (billing@cs.umu.se)

    Updated by Ola Ringdahl 204-09-11
    Updated by Lennart Jern 20016-09-06 (converted to Python 3)
    Updated by Sarah Hale 2017-09-13
    """
    def getPose(self):
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

 