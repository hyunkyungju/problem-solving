import sys
input = sys.stdin.readline

n, c = map(int, input().split())
ips = []
for _ in range(n):
  ips.append(int(input()))
ips.sort()

def check(d):
  cnt = 1
  i = 0
  j = 1
  while i < n-1 and j < n:
    if ips[j] - ips[i] >= d:
      cnt += 1
      i = j
    j += 1
  if cnt >= c:
    return True
  return False
  

lo = 1
hi = (max(ips) - min(ips) + 1)
while lo + 1 < hi:
  mid = (lo + hi) // 2
  if check(mid):
    lo = mid
  else:
    hi = mid
print(lo)