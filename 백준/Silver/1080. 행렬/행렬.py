import sys

input = sys.stdin.readline


n, m = map(int, input().split())
a = [list(map(int, list(input().rstrip()))) for _ in range(n)]
b = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def toggle(i, j):
  for ii in range(3):
    for jj in range(3):
      a[i+ii][j+jj] = int(not a[i+ii][j+jj])

cnt = 0
for i in range(n-2):
  for j in range(m-2):
    
    if a[i][j] != b[i][j]:
      toggle(i, j)
      cnt += 1

if a==b:
  print(cnt)
else:
  print(-1)
  
