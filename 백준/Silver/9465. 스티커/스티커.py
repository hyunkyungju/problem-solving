import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  scores = list()
  scores.append(list(map(int, input().split())))
  scores.append(list(map(int, input().split())))
  dp = [[0]*3 for _ in range(n)]
  dp[0] = [scores[0][0], scores[1][0], 0]
  for i in range(1, n):
    dp[i] = [max(dp[i-1][1], dp[i-1][2])+scores[0][i], 
            max(dp[i-1][0], dp[i-1][2])+scores[1][i], 
            max(dp[i-1][0], dp[i-1][1])]
  print(max(dp[n-1]))
  