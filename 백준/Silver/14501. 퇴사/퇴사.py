import sys
import itertools

input = sys.stdin.readline

n = int(input())
t = [0] * (n + 1)
p = [0] * (n + 1)
for i in range(1, n + 1):
  t[i], p[i] = map(int, input().split())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], dp[i])
    f = i + t[i] - 1
    if f <= n:
        dp[f] = max(dp[f], dp[i-1] + p[i])

print(dp[n])
