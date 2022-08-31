import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
graph = [defaultdict(int) for _ in range(n+1)]
max_ = 2
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = max(graph[a][b], c)
  graph[b][a] = max(graph[b][a], c)
  max_ = max(max_, c)


s, e = map(int, input().split())


def bfs(mid):
  q = deque()
  q.append(s)
  visited = [False] * (n+1)
  visited[s] = True
  
  while q:
    v = q.popleft()
    if v == e:
      return True
    for i, d in graph[v].items():
      if d >= mid and visited[i] == False:
        visited[i] = True
        q.append(i)

lo = 1
hi = max_ + 1
while lo + 1 < hi:
  mid = (lo + hi) // 2
  if bfs(mid):
    lo = mid
  else:
    hi = mid
print(lo)

