import sys
import math

input = sys.stdin.readline

ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())
f_m1 = 0
for _ in range(40):
    m1x = (ax * 2 + bx) / 3
    m1y = (ay * 2 + by) / 3
    m1z = (az * 2 + bz) / 3
    m2x = (ax + bx * 2) / 3
    m2y = (ay + by * 2) / 3
    m2z = (az + bz * 2) / 3

    f_m1 = pow(m1x - cx, 2) + pow(m1y - cy, 2) + pow(m1z - cz, 2)
    f_m2 = pow(m2x - cx, 2) + pow(m2y - cy, 2) + pow(m2z - cz, 2)
    if f_m1 > f_m2:
        ax = m1x
        ay = m1y
        az = m1z
    else:
        bx = m2x
        by = m2y
        bz = m2z
print(math.sqrt(f_m1))