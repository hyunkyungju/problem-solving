import sys
import math

input = sys.stdin.readline


n = int(input())

lst = [9 * math.pow(10, i-1) for i in range(10)]

len_ = len(str(n))
sol = 0
for i in range(1, len_):
  sol += i * lst[i]

sol += (n-math.pow(10, len_-1)+1)*len_
print(int(sol))
