import sys
input = sys.stdin.readline

n = int(input())
b = [[] for _ in range(n)]

max_ = 0

def cal():
  global max_
  # 열에서 
  for i in range(n):
    cnt = 1
    for j in range(n-1):
      if b[i][j] == b[i][j+1]:
        cnt += 1
        max_ = max(max_, cnt)
      else:
        cnt = 1

  # 행에서 
  for i in range(n):
    cnt = 1
    for j in range(n-1):
      if b[j][i] == b[j+1][i]:
        cnt += 1
        max_ = max(max_, cnt)
      else:
        cnt = 1

for i in range(n):
  b[i] = list(input().rstrip())

for i in range(n):
  for j in range(n-1):
    if b[i][j]!=b[i][j+1]:
      b[i][j], b[i][j+1] = b[i][j+1], b[i][j] 
      cal()
      b[i][j+1], b[i][j] = b[i][j], b[i][j+1] 

    if b[j][i]!=b[j+1][i]:
      b[j][i], b[j+1][i] = b[j+1][i], b[j][i] 
      cal()
      b[j+1][i], b[j][i] = b[j][i], b[j+1][i] 


print(max_)
