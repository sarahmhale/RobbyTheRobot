import time

class Timer:
    startTime = 0
    stopTime = 0

    def startTimer(self):
        self.startTime = time.time()

    def stopTimer(self):
        self.stopTime = time.time()

    def printTimer(self):
        if(self.stopTime == 0):
            print ('Time passed ', time.time()-self.startTime, ' secondes')
        else:
            print ('Time passed ', self.stopTime-self.startTime, ' secondes')

    def getTime(self):
        return self.stopTime-self.startTime
