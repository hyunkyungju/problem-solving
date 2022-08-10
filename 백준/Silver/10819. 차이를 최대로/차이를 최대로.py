import sys
import itertools

input = sys.stdin.readline

n = int(input())
ips = list(map(int, input().split()))
max_ = 0
visited = [False] * n


def cal(lst):
    sum_ = 0
    for i in range(n - 1):
        sum_ += abs(lst[i] - lst[i + 1])
    return sum_


def bt(s):
    global max_
    if len(s) == n:
        max_ = max(max_, cal(s))
        return
    for i, v in enumerate(ips):
        if not visited[i]:
            visited[i] = True
            bt(s + [v])
            visited[i] = False


bt([])
print(max_)
