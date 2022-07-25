import sys
input = sys.stdin.readline

def sol(n, d):
  d[1] = 1
  if n==1:
    return
  d[2] = 2
  for i in range(3, n+1):
    d[i] = (d[i-2] + d[i-1]) % 10007
    
n = int(input())
d = [0]*(n+1)

sol(n, d)
print(d[n])