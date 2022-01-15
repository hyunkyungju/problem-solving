# 7
# 3 1 6 2 7 30 1
import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

terminate = 0
for i in range(n):
  value = lst[i]
  if terminate+1<value:
    break
  else:
    terminate = terminate + value
print(terminate+1)
