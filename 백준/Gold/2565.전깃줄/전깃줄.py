import sys

n = int(sys.stdin.readline())
x = list()
for _ in range(n):
  x.append(list(map(int,sys.stdin.readline().split() )))
x.sort(key=lambda x:x[0])

lst = [1]*n
for i in range(n):
  value = x[i][1]
  for j in range(i):
    if x[j][1]<value and lst[j]+1>lst[i]:
      lst[i] = lst[j]+1
print(n-max(lst))
