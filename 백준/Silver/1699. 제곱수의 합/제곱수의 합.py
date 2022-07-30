import sys
import math
input = sys.stdin.readline

n = int(input())
lst = [n]*(n+1)
for i in range(1, int(math.sqrt(n))+1):
  lst[int(math.pow(i, 2))]=1
for i in range(1, n+1):
  min_ = lst[i]
  for j in range(1, int(math.sqrt(i))+1):
    min_ = min(min_, lst[i-int(math.pow(j, 2))]+1)
  lst[i] = min_
print(lst[n])