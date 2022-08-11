import sys
import itertools

input = sys.stdin.readline

n = int(input())
ips = list(input().split())
min_ = str(9) * (n + 1)
max_ = str(0) * (n + 1)
visited = [False] * 10


def bt(s):
    global min_
    global max_
    if len(s) == n + 1:
        s_int = ''.join(map(str, s))
        min_ = min(min_, s_int)
        max_ = max(max_, s_int)
        return
    a, b = 0, 0
    if ips[len(s) - 1] == '<':
        a, b = s[-1] + 1, 10
    else:
        a, b = 0, s[-1]

    for i in range(a, b):
        if not visited[i]:
            visited[i] = True
            bt(s + [i])
            visited[i] = False


for i in range(10):
    visited[i] = True
    bt([i])
    visited[i] = False
print(max_)  
print(min_)

