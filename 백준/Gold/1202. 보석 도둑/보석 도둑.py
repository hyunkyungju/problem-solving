import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
js = []
for _ in range(n):
    m, v = map(int, input().split())
    js.append((m, v))
js.sort(reverse=True)

bags = []
for _ in range(k):
    bags.append(min(1000000, int(input())))
bags.sort()

small_js = []
total = 0
for bag in bags:
    while js and js[-1][0] <= bag:
        heapq.heappush(small_js, -js.pop()[1])
    if small_js:
        total += -heapq.heappop(small_js)
    elif not js:
        break

print(total)
