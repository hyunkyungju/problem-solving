import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n - 1):
  a, b, d = map(int, input().split())
  graph[a].append((b, d))
  graph[b].append((a, d))
  

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