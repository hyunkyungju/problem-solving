import sys
input = sys.stdin.readline

n = int(input())
ips = list()
for i in range(n):
  ips.append((i, int(input())))
ips.sort(key = lambda x: x[1])

ans = 1
for i, (fi, value) in enumerate(ips):
  ans = max(ans, fi - i + 1)
print(ans)