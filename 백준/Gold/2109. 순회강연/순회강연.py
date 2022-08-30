import sys
import heapq

input = sys.stdin.readline

n = int(input())
if not n:
  print(0)
  exit()
ips = []
for _ in range(n):
  p, d = map(int, input().split())
  ips.append((p, d))
ips.sort(key=lambda x:x[1])
max_d = max(ips, key=lambda x:x[1])[1]

total = 0
tmp_p = []
for i in range(max_d, 0, -1):
  while ips and ips[-1][1] == i:
    heapq.heappush(tmp_p, -ips.pop()[0])
  if tmp_p:
    total += -heapq.heappop(tmp_p)
  elif not ips:
    break
print(total)