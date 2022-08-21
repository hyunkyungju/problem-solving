import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
if n >= k:
    print(n - k)
    exit()

max_ = k * 2
lst = [-1] * (max_ + 1)

q = deque()
q.append(n)
lst[n] = 0

while q:
    x = q.popleft()
    l = lst[x]

    if x == 0:
        if lst[x + 1] == -1:
            lst[x + 1] = l + 1
            q.append(x + 1)
        continue

    while x < max_:
        if x == k:
            print(l)
            exit()
        if lst[x] == -1:
            lst[x] = l

        if lst[x - 1] == -1:
            lst[x - 1] = l + 1
            q.append(x - 1)

        if lst[x + 1] == -1:
            lst[x + 1] = l + 1
            q.append(x + 1)

        x = x * 2
