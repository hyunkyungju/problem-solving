import sys
import math

input = sys.stdin.readline

max_num = 1000000
lst = [False]*(max_num+1)
for i in range(2, int(math.sqrt(max_num))+1):
  for j in range(2, max_num//i+1):
    lst[i*j] = True

t = int(input())
for _ in range(t):
  n = int(input())
  cnt = 0
  for i in range(2, n//2+1):
    if not lst[i] and not lst[n-i]:
      cnt+=1
  print(cnt)
    