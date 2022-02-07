import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [set([]) for _ in range(n+1)]
for _ in range(m):
  front, back = map(int, input().split())
  graph[front].add(back)

visited = [False]*(n+1)
results = list()

def topo(start):
  for v in graph[start]:
    if not visited[v]:
      visited[v] = True
      topo(v)
  results.append(start)


for i in range(1, n+1):
  if not visited[i]:
    visited[i]=True
    topo(i)


results.reverse()
for number in results:
  print(number, end=' ')