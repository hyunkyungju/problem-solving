import sys
import itertools

input = sys.stdin.readline

n, s = map(int, input().split())
ips = sorted(list(map(int, input().split())))
cnt = 0
visited = [False] * n


def bt(st, index, sum_):
    global cnt
    new_sum = sum_ + st[-1]
    if new_sum == s:
        cnt += 1
    for i in range(index + 1, n):
        bt(st + [ips[i]], i, new_sum)


for i, v in enumerate(ips):
    bt([v], i, 0)
print(cnt)
