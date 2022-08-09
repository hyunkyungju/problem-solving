import sys
input = sys.stdin.readline

n = int(input())

prices = [[0, 0, 0] for _ in range(n)]

for i in range(n):
  prices[i] = list(map(int, input().split()))

dp = [[0, 0, 0] for _ in range(n)]
INF = 1e9
sol = INF
for color in range(3):
  dp[0] = [INF, INF, INF]
  dp[0][color] = prices[0][color] 
  for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2])+prices[i][0] 
    dp[i][1] = min(dp[i-1][0], dp[i-1][2])+prices[i][1] 
    dp[i][2] = min(dp[i-1][0], dp[i-1][1])+prices[i][2] 
  for i in range(3):
    if i != color:
      sol = min(sol,dp[n-1][i])
print(sol)