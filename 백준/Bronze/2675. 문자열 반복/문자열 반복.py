import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
  iter, s = input().split()
  iter = int(iter)
  s = list(s)
  for c in s:
    for _ in range(iter):
      print(c, end = '')
  print()