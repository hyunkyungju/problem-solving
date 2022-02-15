import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijk(start):
  q = []
  distance = [INF]*(n+1)
  distance[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for v, edge in graph[now]:
      new_distance = dist + edge
      if distance[v] > new_distance:
        distance[v] = new_distance
        heapq.heappush(q, (new_distance, v))
  return distance

n, m= map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  u, v, w = map(int, input().split())
  is_in_graph = False
  for i in range(len(graph[u])):
    vertex, weight = graph[u][i]
    if vertex==v:
      if weight<w:
        is_in_graph = True
      else:
        del graph[u][i]
      break
  if not is_in_graph: 
    graph[u].append((v,w))
distance = dijk(start)

for i in range(1, n+1):
  dist = distance[i]
  if dist ==INF:
    print("INF")
  else:
    print(dist)