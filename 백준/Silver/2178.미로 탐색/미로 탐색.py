import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

start = list([0, 0])
queue = deque([start])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx and nx<n and 0<=ny and ny<m and graph[nx][ny]==1:
      queue.append(list([nx, ny]))
      graph[nx][ny]=graph[x][y]+1

print(graph[n-1][m-1])
