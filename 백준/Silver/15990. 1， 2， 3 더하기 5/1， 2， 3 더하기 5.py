import sys
input = sys.stdin.readline

t = int(input())
lst = [0]*(t)
for i in range(t):
  lst[i] = int(input())
n = max(lst)
n = max(n, 3)

dp = [0]*(n+1)
dp[1] = (1, 0, 0)
dp[2] = (0, 1, 0)
dp[3] = (1, 1, 1)
for i in range(4, n+1):
  dp[i] = ((dp[i-1][1]+dp[i-1][2]) % 1000000009, (dp[i-2][0]+dp[i-2][2]) % 1000000009, (dp[i-3][0]+dp[i-3][1]) % 1000000009) 

for test in lst:
  print(sum(dp[test]) % 1000000009 )
