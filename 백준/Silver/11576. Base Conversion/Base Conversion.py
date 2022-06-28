import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input())
lst = list(map(int, input().split()))
d = 0

for i, n in enumerate(reversed(lst)):
  d += n * pow(a, i)

results = list()
while d >= b:
  results.append(d%b)
  d = d//b
results.append(d)
print(' '.join(map(str, reversed(results))))
