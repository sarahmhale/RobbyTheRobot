import unittest

from Timer import Timer

class TimerTest(unittest.TestCase):
    def test_timeShouldBeZeroFromBeginning(self):
        Time = Timer()
        self.assertEqual(Time.getTime(), 0)

    def test_timeShouldNotBeZeroEfterStartTime(self):
        Time = Timer()
        Time.startTimer()
        self.assertNotEqual(Time.getTime(), 0)

    def test_timeShouldBeStopped(self):
        Time = Timer()
        Time.startTimer()
        Time.printTimer()
        Time.stopTimer()
        firstTime = Time.getTime()
        self.assertEqual( firstTime, Time.getTime())


if __name__ == '__main__':
    unittest.main()
