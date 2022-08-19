import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
if n == k:
  print(0)
  print(n)
  exit()

q = deque()
min_ = 0
max_ = 100000
parents = [-1] * (max_ + 1)
parents[n] = [n]
q.append((n, 0)) 


def print_path(x):
  path = list()
  while x != n:
    path.append(x)
    x = parents[x]
  path.append(n)
  print(*reversed(path))
  

def check_insert(x, l, p):
  if x < min_ or x > max_ or parents[x] != -1:
    return
  parents[x] = v
  if x == k:
    print(l+1)
    print_path(x)
    exit()
  q.append((x, l+1))
  
while q:
  v, l = q.popleft()
  check_insert(2 * v, l, v)
  check_insert(v + 1, l, v)
  check_insert(v - 1, l, v)
  