from math import *
from moment import Moment

class Earth:

    def __init__(self, moment):
        self.moment = moment

    def mean_anomaly(self):
        M = 357.529 + 0.9856003 * self.moment.day_d()
        M %= 360
        return M

    def equation_of_center(self):
        M = self.mean_anomaly()
        A = 1.915 * sin(radians(M)) + 0.020 * sin(2 * radians(M))
        return A

    def eccentricity(self):
        t = self.moment.time_t()
        e = 0.016708634 - (0.000042037 * t) - (0.0000001267 * t**2)
        return e

    def radius_vector(self):
        M = self.mean_anomaly()
        R = 1.00014 - 0.01671 * cos(radians(M)) - 0.00014 * cos(2 * radians(M))
        return R


class Jupiter:

    def __init__(self, moment):
        self.moment = moment

    def t1(self):
        d = self.moment.julian_day() - 2433282.5
        return d / 36525

    def long_period_term(self):
        return 172.74 + 0.00111588 * self.moment.day_d()

    def mean_anomaly(self):
        return 20.020 + 0.0830853 * self.moment.day_d() + 0.329 * sin(radians(self.long_period_term()))

    def equation_of_center(self):
        N = self.mean_anomaly()
        B = 5.555 * sin(radians(N)) + 0.168 * sin(2 * radians(N))
        return B

    def delta_heliocentric(self):
        J = 66.115 + 0.9025179 * self.moment.day_d() - 0.329 * sin(radians(self.long_period_term()))
        J %= 360
        return J

    def radius_vector(self):
        N = self.mean_anomaly()
        r = 5.20872 - 0.25208 * cos(radians(N)) - 0.00611 * cos(2 * radians(N))
        return r


