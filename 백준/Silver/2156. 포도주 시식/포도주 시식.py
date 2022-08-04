import sys

input = sys.stdin.readline

n = int(input())
lst = [0]*n
for i in range(n):
  lst[i] = int(input())

dp = [[0,0,0] for _ in range(n)]
dp[0] = [0, lst[0], 0]
for i in range(1, n):
  dp[i] = [max(dp[i-1]), dp[i-1][0]+lst[i], dp[i-1][1]+lst[i]]
print(max(dp[n-1]))