import sys
n, m, s = map(int, sys.stdin.readline().split())
lst=list()
for i in range(0, n):
  lst.append(list(map(int, sys.stdin.readline().split())))
start = -1
lst.sort()


if lst[0][0] >= m:
  start = 0
else:
  for i in range(1, n):
   if lst[i][0] - (lst[i-1][0]+lst[i-1][1]) >= m:
     start = lst[i-1][0]+lst[i-1][1]
     break
if start==-1 and s - (lst[n-1][0]+lst[n-1][1]) >= m:
  start = lst[n-1][0]+lst[n-1][1]
print(start)