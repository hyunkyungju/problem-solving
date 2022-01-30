import sys
t = int(sys.stdin.readline())
lst = list()
for _ in range(t):
  lst.append(int(sys.stdin.readline()))
maximum = max(lst)

dp = [1]*(maximum+1)
for i in range(maximum-2, -1, -1):
  dp[i] = dp[i+1]+dp[i+2]
for i in range(t):
  value = lst[i]
  if value==0:
    print(1, 0)
  elif value==1:
    print(0, 1)
  else:
    index = maximum-value
    print(dp[index+2],dp[index+1])
