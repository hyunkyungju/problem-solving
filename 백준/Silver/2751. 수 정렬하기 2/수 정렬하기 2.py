import sys
input = sys.stdin.readline

n = int(input())
ips = list()
for _ in range(n):
  ips.append(int(input()))
ips.sort()
for i in ips:
  print(i)
