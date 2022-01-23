# 최소 강의실의 개수를 출력하라.

import heapq
import sys

n = int(sys.stdin.readline())
lst = list()
for _ in range(n):
  lst.append(list(map(int, sys.stdin.readline().split( ))))
lst.sort()
heap = []
heapq.heappush(heap, lst[0][1])
for i in range(1, n):
  start, finish = lst[i][0], lst[i][1]
  reservation = heap[0]
  if reservation <= start: # 여기 들어가기 
    heapq.heappush(heap, finish)
    heapq.heappop(heap)
  else:
    heapq.heappush(heap, finish)
print(len(heap))


#2h 32m 5s