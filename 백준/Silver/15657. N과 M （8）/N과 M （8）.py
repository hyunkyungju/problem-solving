import sys
import itertools

input = sys.stdin.readline

n, m = map(int, input().split())
ips = sorted(list(map(int, input().split())))


def bt(s):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for v in ips:
        if v >= s[-1]:
            bt(s + [v])


for v in ips:
    bt([v])