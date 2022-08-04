import sys

input = sys.stdin.readline

n = int(input())
dp = [[0]*10 for _ in range(n+1)]
dp[1] = [1]*10

for i in range(2, n+1):
  sum_ = 0
  for j in range(0, 10):
    sum_ += dp[i-1][j]
    sum_ %= 10007
    dp[i][j] = sum_ 

print(sum(dp[n])% 10007)