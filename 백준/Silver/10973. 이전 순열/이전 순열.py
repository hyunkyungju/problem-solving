import sys
import itertools

input = sys.stdin.readline

n = int(input())
ips = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if ips[i - 1] > ips[i]:
        for j in range(n - 1, 0, -1):
            if ips[i - 1] > ips[j]:
                ips[i - 1], ips[j] = ips[j], ips[i - 1]
                ips = ips[:i] + list(reversed(sorted(ips[i:])))
                print(*ips)
                exit()
print(-1)

