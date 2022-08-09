import sys
input = sys.stdin.readline

def sol():
  n = int(input())
  if n % 2 != 0:
    print(0)
    return
  if n==2:
    print(3)
    return
  if n==4:
    print(11) 
    return
  dp = [0]*(n+1)
  dp[2] = 3
  dp[4] = 11
  for i in range(6, n+1, 2):
    sum_ = 2
    for j in range(2, i-2, 2):
      sum_ += dp[j] * 2
    sum_ += dp[i-2] * 3
    dp[i] = sum_    
  print(dp[n])
sol()
