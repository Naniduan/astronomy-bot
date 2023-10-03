from datetime import *
from math import floor

class Moment:

    def __init__(self):
        self.dt = dt
        self.year = -4712
        self.month = 1
        self.day = 1

    def __init__(self, dt):
        self.dt = dt
        self.year = dt.year
        self.month = dt.month
        self.day = dt.day
        hour = dt.hour
        minute = dt.minute
        second = dt.second

        self.day += (1/24) * (hour + (1/60) * (minute + (1/60) * second))

    def julian_day(self):
        Y = self.year
        M = self.month
        D = self.day
        A = Y // 100
        B = 2 - A + A // 4 #A and B are for managing leap years

        if (M in (1,2)):
            Y -= 1
            M += 12

        JD = floor(365.25 * (Y + 4716)) + floor(30.6001 * (M + 1)) + D + B - 1524.5

        return JD

    #days since start of epoch J2000.0
    def day_d(self):
        return self.julian_day() - 2451545.0
    
    #time in Julian centuries of 36525 days
    def time_t(self):
        return (self.julian_day() - 2451545.0) / 36525

    
        
