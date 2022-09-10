import sys
import heapq

input = sys.stdin.readline

def sol():
  n, m = map(int, input().split())
  ips = list(map(int, input().split()))
  h = []
  for i in ips:
    h.append(-i)
  heapq.heapify(h)
  max_ = -heapq.heappop(h)
  while True:
    for i, v in enumerate(ips):
      if not h:
        print(n)
        return
      if max_ == v:
        if i == m:
          print(n-len(h))
          return
        max_ = -heapq.heappop(h)

t = int(input())
for _ in range(t):
  sol()