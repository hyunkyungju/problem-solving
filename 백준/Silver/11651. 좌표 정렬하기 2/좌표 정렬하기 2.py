import sys
input = sys.stdin.readline

n = int(input())
ips = list()
for _ in range(n):
  x, y =  map(int, input().split())
  ips.append((x, y))
ips.sort(key=lambda x:(x[1], x[0]))
for i in ips:
  print(*i)
