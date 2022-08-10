import sys
import math

input = sys.stdin.readline


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def sol():
    m, n, x, y = map(int, input().split())
    lcm_ = lcm(m, n)
    a = x
    b = y
    while a <= lcm_ and b <= lcm_:
        if a == b:
            return a
        elif a > b:
            b += n
        else:
            a += m
    return -1


t = int(input())

for _ in range(t):
    print(sol())
