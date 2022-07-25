import sys
input = sys.stdin.readline

    
n = int(input())
p = list(map(int, input().split()))

d = [0]*(n+1)
for i in range(1, n+1):
  min_ = p[i-1]
  for j in range(1, i//2+1):
    min_ = min(min_, d[i-j]+p[j-1])
  d[i]=min_
print(d[n])
