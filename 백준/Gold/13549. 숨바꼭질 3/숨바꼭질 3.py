import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
if n > k:
  print(n-k)
  exit()

max_ = k * 2
lst = [-1] * (max_ + 1)

q = deque()
q.append(n)
lst[n] = 0

while q:
    x = q.popleft()
    l = lst[x]

    if x == k:
        print(l)
        break

    if x == 0:
      if lst[x+1] == -1:
        lst[x+1] = l + 1
        q.append(x + 1)
      continue
  
    p = x
    while p < max_:
        if p == k:
            print(l)
            exit()
        if lst[p] == -1:
            lst[p] = l

        if lst[p - 1] == -1:
            lst[p - 1] = l + 1
            q.append(p - 1)

        if lst[p + 1] == -1:
            lst[p + 1] = l + 1
            q.append(p + 1)

        p = p * 2
