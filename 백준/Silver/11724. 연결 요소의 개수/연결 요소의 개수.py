import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
cnt = 0


def dfs(s):
    for v in graph[s]:
        if visited[v] == False:
            visited[v] = True
            dfs(v)


for v in range(1, n+1):
    if not visited[v]:
        cnt += 1
        visited[v] = True
        dfs(v)

print(cnt)
