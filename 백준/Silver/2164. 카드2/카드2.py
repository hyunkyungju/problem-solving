import sys
from collections import deque
input = sys.stdin.readline

q = deque()
for i in range(1, int(input()) + 1):
  q.append(i)

while len(q) >= 2:
  q.popleft()
  q.append(q.popleft())

print(q[0])