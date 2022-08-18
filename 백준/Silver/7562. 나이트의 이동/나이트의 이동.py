import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
dr = [1, 1, 2, 2, -1, -1, -2, -2]
dc = [-2, 2, -1, 1, 2, -2, 1, -1]


def sol():
    l = int(input())
    sr, sc = map(int, input().split())
    lr, lc = map(int, input().split())
    if sr == lr and sc == lc:
        print(0)
        return

    q = deque()
    visited = [[False] * l for _ in range(l)]
    visited[sr][sc] = True
    q.append((sr, sc, 0))
    while q:
        hr, hc, hlevel = q.popleft()
        for i in range(8):
            nr = hr + dr[i]
            nc = hc + dc[i]
            if nr < 0 or nr >= l or nc < 0 or nc >= l or visited[nr][
                    nc] == True:
                continue
            if nr == lr and nc == lc:
                print(hlevel + 1)
                return
            visited[nr][nc] = True
            q.append((nr, nc, hlevel + 1))


for _ in range(t):
    sol()
