import sys
import itertools

input = sys.stdin.readline

n = int(input())
ips = [[0] * n for _ in range(n)]
for i in range(n):
    ips[i] = list(map(int, input().split()))
min_ = 1e9 
visited = [False] * n


def all_visit():
    for i in range(n):
        if not visited[i]:
            return False
    return True


def dfs(start, fee):
    global min_
    if all_visit():
        if ips[start][0]:
          min_ = min(min_, fee + ips[start][0])
        return
    for i in range(n):
        if not visited[i] and ips[start][i] != 0:
            visited[i] = True
            dfs(i, fee + ips[start][i])
            visited[i] = False


visited[0] = True
dfs(0, 0)
print(min_)
