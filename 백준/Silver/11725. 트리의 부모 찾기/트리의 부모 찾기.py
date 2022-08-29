import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

parents = [0] * (n + 1)

q = deque()
q.append(1)

while q:
  s = q.popleft()
  for v in graph[s]:
    if parents[v] != 0:
      continue
    parents[v] = s
    q.append(v)

for i, v in enumerate(parents):
  if i == 0 or i == 1:
    continue
  print(v)