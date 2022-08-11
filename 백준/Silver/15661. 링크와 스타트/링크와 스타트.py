import sys
import itertools

input = sys.stdin.readline

n = int(input())
# ips = [[0]*n for _ in range(n)]
ips = [list(map(int, input().split())) for _ in range(n)]
min_ = 10000


def bt(s):
    global min_

    sum_ = 0
    for a, b in itertools.combinations(s, 2):
        sum_ += ips[a][b] + ips[b][a]

    not_s = [x for x in range(n) if x not in s]
    r_sum_ = 0
    for a, b in itertools.combinations(not_s, 2):
        r_sum_ += ips[a][b] + ips[b][a]

    min_ = min(min_, abs(sum_ - r_sum_))

    if len(s) == n - 1:
        return
      
    for i in range(s[-1] + 1, n):
        bt(s + [i])


bt([0])
print(min_)
