import sys

input = sys.stdin.readline

n = int(input())
ips = [list(input().rstrip()) for _ in range(n)]
ips_r = [[''] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if ips[i][j] == 'H':
      ips_r[i][j] = 'T'
    else:
      ips_r[i][j] = 'H'

sol = n*n 

for bf in range(1 << n):
  t = []
  for i in range(n):
    if bf & (1 << i) != 0:
      t.append(ips_r[i])
    else:
      t.append(ips[i])

  total = 0
  for c in range(n):
    cnt = 0
    for r in range(n):
      if t[r][c] == 'T':
        cnt += 1
    total += min(cnt, n-cnt)
  sol = min(sol, total)

print(sol)