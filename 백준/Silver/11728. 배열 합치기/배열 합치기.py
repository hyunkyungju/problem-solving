import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ms = []
ai = 0
bi = 0
while ai < n and bi < m:
  if a[ai] <= b[bi]:
    ms.append(a[ai])
    ai += 1
  else:
    ms.append(b[bi])
    bi += 1    
while ai < n:
  ms.append(a[ai])
  ai += 1
while bi < m:
  ms.append(b[bi])
  bi += 1  
  
print(*ms)