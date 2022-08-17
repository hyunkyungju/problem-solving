import sys
from collections import deque

input = sys.stdin.readline

# m: 가로, n: 세로 
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
cnt = 0
zero = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      zero += 1
    elif graph[i][j] == 1:
      q.append((i, j, 0))

while zero != 0:
  if not q:
    print(-1)
    exit()
  x, y, c = q.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if graph[nx][ny] == 0:
      zero -= 1
      graph[nx][ny] = 1
      q.append((nx, ny, c+1))
      cnt = c+1 
  
print(cnt)