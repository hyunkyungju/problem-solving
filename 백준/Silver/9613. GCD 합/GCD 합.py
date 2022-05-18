import sys
import math

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  lst = list(map(int, input().split()))
  sum = 0
  for i in range(1, len(lst)):
    for j in range(i+1, len(lst)):
      sum += math.gcd(lst[i],  lst[j])
  print(sum)      
    