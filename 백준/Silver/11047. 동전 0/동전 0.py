import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = list()
for _ in range(n):
  c = int(input())
  if c > k:
    continue
  coins.append(c)

coins.reverse()
min_ = 0

for coin in coins:
  min_ += k // coin
  k %= coin
print(min_)
  