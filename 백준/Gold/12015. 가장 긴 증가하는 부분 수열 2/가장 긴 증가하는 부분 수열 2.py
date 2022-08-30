import sys

input = sys.stdin.readline

n = int(input())
ips = list(map(int, input().split()))

lst = [0]

for i in ips:
  if i > lst[-1]:
    lst.append(i)
    continue
  lo = -1
  hi = len(lst)
  while lo + 1 < hi:
    mid = (lo + hi) // 2
    if i <= lst[mid]: # True
      hi = mid
    else:
      lo = mid
  lst[hi] = i

print(len(lst)-1)