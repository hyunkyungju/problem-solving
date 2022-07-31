import sys

input = sys.stdin.readline

t = int(input())

lst = [0] * t
for i in range(t):
    lst[i] = int(input())

max_ = max(lst)
max_ = max(max_, 3)
dp = [0] * (max_ + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, max_ + 1):
    dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1000000009

for test in lst:
    print(dp[test])
