from math import *
from datetime import *
from moment import Moment
from bodies import *

class MoonPositions:

    def __init__(self, io, europa, ganymede, callisto):
        self.io_x = io[0]
        self.io_y = io[1]

        self.europa_x = europa[0]
        self.europa_y = europa[1]

        self.ganymede_x = ganymede[0]
        self.ganymede_y = ganymede[1]

        self.callisto_x = callisto[0]
        self.callisto_y = callisto[1]

        self.as_list = [io, europa, ganymede, callisto]

def correct_degree_range(angle):
    if angle < 0: angle+=360
    angle %= 360
    return angle

def get_moons_position(dt):
    moment = Moment(dt)
    earth = Earth(moment)
    jupiter = Jupiter(moment)

    d = moment.day_d()
    V = jupiter.long_period_term()
    J = jupiter.delta_heliocentric()
    A = earth.equation_of_center()
    B = jupiter.equation_of_center()
    K = J + A - B
    if K < 0: K += 360

    R = earth.radius_vector()
    r = jupiter.radius_vector()

    delta = sqrt(r**2 + R**2 - 2 * r * R * cos(radians(K)))
    psi = asin(R / delta * sin(radians(K)))
    psi_angle = degrees(psi)

    lambda_angle = 34.35 + 0.083091 * d + 0.329 * sin(radians(V)) + B

    Ds = 3.12 * sin(radians(lambda_angle) + 0.74700091985)
    Dx = 2.22 * sin(radians(psi_angle)) * cos(radians(lambda_angle) + 0.38397243544)
    Dy = 1.30 * ((r - delta) / delta) * sin(radians(lambda_angle) - 1.7540558983)

    De = Ds - Dx - Dy

    t = delta / 173

    u1 = 163.8069 + 203.4058646 * (d - t) + psi_angle - B
    u2 = 358.4140 + 101.2916335 * (d - t) + psi_angle - B
    u3 = 5.7176 + 50.2345180 * (d - t) + psi_angle - B
    u4 = 224.8092 + 21.4879800 * (d - t) + psi_angle - B

    u1 = correct_degree_range(u1)
    u2 = correct_degree_range(u2)
    u3 = correct_degree_range(u3)
    u4 = correct_degree_range(u4)

    G = 331.18 + 50.310482 * (d - t)
    H = 87.45 + 21.569231 * (d - t)

    r1 = 5.9057 - 0.0244 * cos(2 * radians(u1-u2))
    r2 = 9.3966 - 0.0882 * cos(2 * radians(u2-u3))
    r3 = 14.9883 - 0.0216 * cos(radians(G))
    r4 = 26.3627 - 0.1939 * cos(radians(H))

    #Io
    x1 = r1 * sin(radians(u1))
    y1 = -r1 * cos(radians(u1)) * sin(radians(De))
    #Europa
    x2 = r2 * sin(radians(u2))
    y2 = -r2 * cos(radians(u2)) * sin(radians(De))
    #Ganymede
    x3 = r3 * sin(radians(u3))
    y3 = -r3 * cos(radians(u3)) * sin(radians(De))
    #Callisto
    x4 = r4 * sin(radians(u4))
    y4 = -r4 * cos(radians(u4)) * sin(radians(De))

    return MoonPositions([x1,y1], [x2,y2], [x3,y3], [x4,y4])

#dt = datetime(2020, 2, 16)
#moon_pos = get_moons_position(dt)

#for moon in moon_pos.as_list:
#    print(moon[0], moon[1])
