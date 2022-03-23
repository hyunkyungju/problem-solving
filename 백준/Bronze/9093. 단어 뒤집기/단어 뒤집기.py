import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
  ss = input().split()
  for s in ss:
    lst = list(s)
    lst.reverse()
    s = ''.join(lst)
    print(s, end=' ')
  print()