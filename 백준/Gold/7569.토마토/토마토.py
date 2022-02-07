import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(h)]

for k in range(h):
  for j in range(n):
    graph[k][j] = list(map(int, input().rstrip().split()))

# h -> n -> m 순서대로 가야함 

def is_ripen():
  for k in range(h):
    for j in range(n):
      for i in range(m):
        if graph[k][j][i] == 0:
          return False
  return True

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

unripen = 0
lst = list()
for k in range(h):
  for j in range(n):
    for i in range(m):
      if graph[k][j][i]==1:
        lst.append(list([i, j, k]))
      elif graph[k][j][i]==0:
        unripen +=1
if unripen == 0:
  print(0)
  lst.clear()

cnt = 0

if not lst and unripen>0:
  print(-1)

while lst:
  nlst = list()
  change = 0
  for i, j, k in lst:    
    for d in range(6):
      nx = i + dx[d]
      ny = j + dy[d]
      nz = k + dz[d]
      if nx in range(m) and ny in range(n) and nz in range(h) and graph[nz][ny][nx]==0:
        graph[nz][ny][nx]=1
        nlst.append(list([nx, ny, nz]))
        change +=1
  cnt +=1
  unripen -= change
  if unripen == 0:
    print(cnt)
    break;
  if change == 0:
    print(-1)
    break;
  lst = nlst

