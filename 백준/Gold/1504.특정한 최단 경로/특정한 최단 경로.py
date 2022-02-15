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
graph = [[] for _ in range(n+1)]
for _ in range(m):
  u, v, w = map(int, input().split())
  graph[u].append((v,w))
  graph[v].append((u,w))
v1, v2 = map(int, input().split())
v0_distance = dijk(1)
v1_distance = dijk(v1)
v2_distance = dijk(v2)

result = min(v0_distance[v1]+v1_distance[v2]+ v2_distance[n], 
      v0_distance[v2]+v2_distance[v1]+ v1_distance[n])
if result<INF:
  print(result)
else:
  print(-1)