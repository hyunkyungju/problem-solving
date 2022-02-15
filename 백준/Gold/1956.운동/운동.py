import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
  a, b, w = map(int, input().split())
  graph[a][b]=min(graph[a][b], w)
  # 어떤 문제는 중복이 들어올 수도 있고 어떤 문제는 아닌건가.. 


for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

result = INF
for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j]<INF and graph[j][i]<INF:
      result = min(result,graph[i][j]+graph[j][i])

if result==INF:
  print(-1)
else:
  print(result)