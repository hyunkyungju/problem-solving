import sys

n, k = map(int,sys.stdin.readline().split())
items = list()
for _ in range(n):
  items .append(list(map(int,sys.stdin.readline().split())))

table = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
  weight = items[i-1][0]
  value = items[i-1][1]
  for j in range(1, min(weight, k+1)):
    table[i][j] = table[i-1][j]
  for j in range(weight, k+1):
    table[i][j] = max(table[i-1][j], table[i-1][j-weight]+value)
print(table[n][k])
