import sys
input = sys.stdin.readline

n = int(input())
ips = list()
for _ in range(n):
  x, y =  input().split()
  ips.append((int(x), y))
ips.sort(key=lambda x: x[0])
for i in ips:
  print(*i)
