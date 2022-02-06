import sys
from collections import deque
input = sys.stdin.readline
n=int(input()) 
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = list()

def bfs(x, y):
  cnt = 1
  queue = deque([(x, y)])
  graph[x][y]=0
  
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx and nx<n and 0<=ny and ny<n and graph[nx][ny]==1:
        graph[nx][ny]=0
        queue.append((nx, ny))
        cnt +=1
  result.append(cnt)

call_bfs = 0
for i in range(n):
  for j in range(n):
    if graph[i][j]==1:
      bfs(i, j)
      call_bfs +=1

print(call_bfs)
result.sort()
for i in result:
  print(i)