import sys
input = sys.stdin.readline

    
d = [1]*(11)
d[2] = 2
for i in range(3, 11):
  d[i] = d[i-3] + d[i-2] + d[i-1]
    
t = int(input())
for _ in range(t):
  print(d[int(input())])