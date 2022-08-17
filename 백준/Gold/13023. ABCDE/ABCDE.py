import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n


def dfs(v, num):
    if num == 4:
        print(1)
        exit()

    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i, num + 1)
            visited[i] = False


for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
