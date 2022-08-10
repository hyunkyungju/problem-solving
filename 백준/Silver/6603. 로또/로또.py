import sys
import itertools

input = sys.stdin.readline

c = 0
ips = list()


def bt(s):
    if len(s) == 6:
        print(*s)
        return
    for v in ips[ips.index(s[-1]) + 1:]:
        bt(s + [v])


def sol(ips):
    for i in range(c - 5):
        bt([ips[i]])


while True:
    ips = list(map(int, input().split()))
    c = ips.pop(0)
    if not c:
        break
    sol(ips)
    print()
