# 파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 

import sys
from collections import deque
input = sys.stdin.readline
INF = 10000001
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  parent, child, weight = map(int, input().split())
  graph[parent].append((child, weight))
  graph[child].append((parent,weight))

def bfs(start):
  queue = deque([start])
  weight = [-1] * (n+1)
  weight[start] = 0
  while queue:
    v = queue.popleft()
    for u, w in graph[v]:
      if weight[u]==-1:
        weight[u] = weight[v]+w
        queue.append(u)
  maximum = max(weight)
  idx = weight.index(maximum)
  return (idx, maximum)

v_on_radius, weight_from_root = bfs(1)
a, b = bfs(v_on_radius)
print(b)
