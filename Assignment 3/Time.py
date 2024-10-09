class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def addTime(self, x):
        totalHours = self.hours + x.hours
        totalMin = self.minutes + x.minutes
        return Time(totalHours,totalMin)
    def displayTime(self):
        print(f"{self.hours} hour and {self.minutes} min")
    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"{total_minutes} minutes")

time1 = Time(2, 50) 
print(time1.displayTime())
time2 = Time(1, 20)
print(time2.displayTime())
time3 = time1.addTime(time2)
print(time3.displayTime())
print(time1.displayMinute())
print(time2.displayMinute())
print(time3.displayMinute())


