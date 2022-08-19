import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
if n == k:
  print(0)
  exit()
q = deque()
min_ = 0
max_ = 100000
visited = [False] * (max_ + 1)
q.append((n, 0))

def check_insert(x, l):
  if x < min_ or x > max_ or visited[x]:
    return
  if x == k:
    print(l+1)
    exit()
  visited[x] = True
  q.append((x, l+1))
  
while q:
  v, l = q.popleft()
  check_insert(2 * v, l)
  check_insert(v + 1, l)
  check_insert(v - 1, l)