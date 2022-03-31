from collections import deque

import sys

input = sys.stdin.readline
q = deque()
n, k = map(int, input().split())
for i in range(n):
  q.append(i+1)
cnt = 1
lst = list()
while len(lst)!=n:
  if cnt== k:
    lst.append(q.popleft())
    cnt = 1
  else:
    q.append(q.popleft())
    cnt +=1

print("<", end='')
for i in range(len(lst)):
  if i==len(lst)-1:
    print(lst[i], end=">")
  else:
    print(lst[i], end=", ")
  