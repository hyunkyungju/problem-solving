import sys

input = sys.stdin.readline

ips = list(map(int, list(input().rstrip())))
if sum(ips) % 3 != 0 or ips.count(0) == 0:
  print(-1)
  exit()

ips.sort(reverse=True)
print(''.join(map(str, ips)))
