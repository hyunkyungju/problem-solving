# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

import sys
from collections import deque
input = sys.stdin.readline
n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
  v1, v2 = map(int, input().split())
  if not v2 in graph[v1]:
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False]*(n+1)
for i in range(n+1):
  graph[i].sort()

def dfs(v):
  visited[v]=True
  print(v, end=' ')
  for u in graph[v]:
    if not visited[u]:
      dfs(u)

def bfs(start):
  visited = [False] * (n+1)
  queue = deque([start])
  visited[start]=True
  print(start, end=' ') 
  while queue:
    v = queue.popleft()
    for u in graph[v]:
      if not visited[u]:
        visited[u]=True
        queue.append(u)
        print(u, end=' ') 
  
dfs(start)
print()
bfs(start)