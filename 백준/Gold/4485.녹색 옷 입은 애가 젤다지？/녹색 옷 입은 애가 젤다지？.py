import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijk(start, n):
  q = []
  distance = [INF]*(n)
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
  return distance[n-1]

def calculate(num, graph):
  lst = []
  for i in range(num):
    lst.append(list(map(int, input().split())))
  for x in range(num):
    for y in range(num):
      index = x*num + y
      for j in range(4):
        nx = x+dx[j]
        ny = y+dy[j]
        if 0<=nx and nx<num and 0<=ny and ny<num:
          graph[index].append([nx*num + ny, lst[nx][ny]])
  return dijk(0, num*num)+lst[0][0]

cnt = 1
while True:
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  num = int(input())
  graph = [[] for _ in range(num*num)]
  if num!=0:
    print("Problem "+str(cnt)+": "+str(calculate(num, graph)))
    cnt +=1
  else:
    break
