import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = [[1]*(k+1) for _ in range(n+1)]

for i in range(2, k+1):
  sum = 1
  for j in range(1, n+1):
    sum += lst[j][i-1] 
    sum %= 1000000000
    lst[j][i] = sum
print(lst[n][k])