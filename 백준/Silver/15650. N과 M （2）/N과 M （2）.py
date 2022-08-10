import sys
import itertools

input = sys.stdin.readline

n, m = map(int, input().split())


def bt(s):
    if len(s) == m+1:
        s.pop(0)
        print(' '.join(map(str, s)))
        return
    for i in range(s[-1] + 1, n + 1):
        bt(s + [i])

bt([0])
