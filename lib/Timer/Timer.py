import time

class Timer:
    startTime = 0
    stopTime = 0

    def startTimer(self):
        self.startTime = time.time()

    def stopTimer(self):
        self.stopTime = time.time()
        print ('Time passed ', self.stopTime-self.startTime, ' secondes')
    