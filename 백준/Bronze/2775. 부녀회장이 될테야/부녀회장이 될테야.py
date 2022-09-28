import sys
input = sys.stdin.readline

t = int(input())
klst = []
nlst = []
for _ in range(t):
  k = int(input())
  klst.append(k)
  n = int(input())
  nlst.append(n)

kmax = max(klst)
nmax = max(nlst)
lst = [[0] * (nmax+1) for _ in range(kmax+1)]

lst[0] = [i for i in range(nmax+1)]
for i in range(1, kmax+1):
  sum_ = 0
  for j in range(1, nmax+1):
    sum_ += lst[i-1][j]
    lst[i][j] = sum_

for i in range(len(klst)):
  k = klst[i]
  n = nlst[i]
  print(lst[k][n])