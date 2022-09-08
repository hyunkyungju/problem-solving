import sys
import math

input = sys.stdin.readline

n, k = map(int, input().split())
lst = [i for i in range(1, n+1)]

print("<", end='')
t = k-1
a = lst.pop(t)

while lst:
  print(str(a)+",", end=' ')
  t = (t + k - 1) % len(lst)
  a = lst.pop(t)
print(str(a)+">")