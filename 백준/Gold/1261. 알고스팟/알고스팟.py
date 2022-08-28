import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

ips = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

q = deque()
q.append((0, 0))
dist[0][0] = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
while q:
  r, c = q.popleft()
  d = dist[r][c]
  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    if nr < 0 or nr >= n or nc < 0 or nc >= m or dist[nr][nc] != -1:
      continue
    if ips[nr][nc] == 0:
      q.appendleft((nr, nc))
      dist[nr][nc] = d
    else:
      q.append((nr, nc))
      dist[nr][nc] = d + 1

print(dist[n-1][m-1])
  