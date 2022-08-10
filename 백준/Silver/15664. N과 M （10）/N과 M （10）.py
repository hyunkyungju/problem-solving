import sys
import itertools

input = sys.stdin.readline

n, m = map(int, input().split())
ips = sorted(list(map(int, input().split())))
visited = [False] * n


def bt(s):
    if len(s) == m + 1:
        s.pop(0)
        print(' '.join(map(str, s)))
        return
    before = 0
    for i, v in enumerate(ips):
        if before != v and not visited[i] and s[-1] <= v:
            visited[i] = True
            before = v
            bt(s + [v])
            visited[i] = False


bt([0])
