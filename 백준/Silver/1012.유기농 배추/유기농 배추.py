import sys
from collections import deque
input = sys.stdin.readline

def calculate(graph, n, m):
  call_bfs = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j]==1:
        bfs(graph, i, j)
        call_bfs +=1
  print(call_bfs)
    
def bfs(graph, x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  queue = deque([(x, y)])
  graph[x][y]=0
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx and nx<n and 0<=ny and ny<m and graph[nx][ny]==1:
        graph[nx][ny]=0
        queue.append((nx, ny))

t=int(input()) 
for i in range(t):
  m, n, k = map(int, input().split()) # n이 세로, m이 가로임
  graph = [[0]*m for _ in range(n)]
  for _ in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1
  calculate(graph, n, m)
