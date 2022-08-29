import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
  lst = list(map(int, input().split()))
  v = lst[0]
  for i in range(1, len(lst) -1 , 2):
    i, d = lst[i], lst[i + 1]
    graph[v].append((i, d))


visited = [False] * (n + 1) 
max_ = 0
x = 0

def dfs(v, ds):
  global max_
  global x
  for i, d in graph[v]:
    if visited[i]:
      continue
    visited[i] = True
    dfs(i, ds + d)
    visited[i] = False
  if max_ < ds:
    max_ = ds
    x = v
    
s = 1
visited[s] = True
dfs(s, 0)
visited[s] = False

visited[x] = True
dfs(x, 0)
visited[x] = False

print(max_)