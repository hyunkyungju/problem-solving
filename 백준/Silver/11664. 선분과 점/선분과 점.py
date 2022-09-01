import sys
import math

input = sys.stdin.readline

ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())

while True:
    m1x = (ax * 2 + bx) / 3
    m1y = (ay * 2 + by) / 3
    m1z = (az * 2 + bz) / 3
    m2x = (ax + bx * 2) / 3
    m2y = (ay + by * 2) / 3
    m2z = (az + bz * 2) / 3

    f_m1 = math.sqrt(pow(m1x - cx, 2) + pow(m1y - cy, 2) + pow(m1z - cz, 2))
    f_m2 = math.sqrt(pow(m2x - cx, 2) + pow(m2y - cy, 2) + pow(m2z - cz, 2))
    diff = math.sqrt(pow(m1x - m2x, 2) + pow(m1y - m2y, 2) + pow(m1z - m2z, 2))
    if diff < 1e-7 and abs(f_m1 - f_m2) < 1e-7:
        print(f_m1)
        break
    if f_m1 > f_m2:
        ax = m1x
        ay = m1y
        az = m1z
    else:
        bx = m2x
        by = m2y
        bz = m2z
