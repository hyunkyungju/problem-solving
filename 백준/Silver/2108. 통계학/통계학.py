import sys
import heapq

input = sys.stdin.readline

n = int(input())
ips = []
for _ in range(n):
  ips.append(int(input()))

ips.sort()
i = 0
max_cnt = 0
max_v_1 = ips[0]
max_v_2 = ips[0] - 1
max_lst = []
cnt = 1
while i < n - 1:
  while i < n -1 and ips[i] == ips[i+1]:
    cnt += 1
    i += 1
  if max_cnt < cnt:
    max_cnt = cnt
    max_v_1 = ips[i]
  elif max_cnt == cnt:
    if max_v_2 < max_v_1:
      max_v_2 = ips[i]
  cnt = 1
  i += 1
print(round(sum(ips)/len(ips)))
print(ips[(n//2)])
print(max(max_v_1, max_v_2))
print(ips[-1]-ips[0])