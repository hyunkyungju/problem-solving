import sys
from collections import deque

input = sys.stdin.readline


def bfs(l, s):
    global is_bi
    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if l[i] == -1:
                l[i] = 0 if l[v] == 1 else 1
                q.append(i)
            elif l[i] == l[v]:
                is_bi = False
                return


k = int(input())
for _ in range(k):
    vn, en = map(int, input().split())
    graph = [[] for _ in range(vn + 1)]
    for _ in range(en):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    l = [-1] * (vn + 1)
    is_bi = True
    for v in range(vn):
        if l[v] == -1 and is_bi:
            l[v] = 0
            bfs(l, v)
    if is_bi:
        print("YES")
    else:
        print("NO")
