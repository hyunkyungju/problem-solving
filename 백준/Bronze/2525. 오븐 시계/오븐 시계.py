import sys

input = sys.stdin.readline

def BOJ2089():
  cal = 0
  n = int(input())
  if n==0:
    print(n)
    return
  bd = 1 if (n>0) else -2
  bd_accum = bd
  while abs(bd_accum) < abs(n):
    bd *=4
    bd_accum +=bd
  cal +=bd
  print("1", end='')
  while cal !=n:
    bd //=-2
    if abs(cal + bd-n) <= abs(cal - n):
      cal +=bd
      print("1", end='')
    else:
      print("0", end='')
  
  while bd !=1:
    bd //= -2
    print("0", end='')

# BOJ2089()

h, m = map(int, input().split())
c = int(input())
h += (c+m)//60
if h>=24:
  h = h-24 
m = (m+c)%60
print(f"{h} {m}")