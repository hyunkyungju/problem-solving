import sys
import itertools

input = sys.stdin.readline

n, m = map(int, input().split())
ips = sorted(list(map(int, input().split())))
visited = [False] * n


def bt(s):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    before = 0
    for i, v in enumerate(ips):
        if before != v and not visited[i]:
            visited[i] = True
            before = v
            bt(s + [v])
            visited[i] = False


bt([])
