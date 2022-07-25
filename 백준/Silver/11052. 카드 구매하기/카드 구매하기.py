import sys
input = sys.stdin.readline

    
n = int(input())
p = list(map(int, input().split()))

d = [0]*(n+1)
for i in range(1, n+1):
  max_ = p[i-1]
  for j in range(1, i//2+1):
    max_ = max(max_, d[i-j]+p[j-1])
  d[i]=max_
print(d[n])
