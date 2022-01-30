import sys

def sol():
  n = int(sys.stdin.readline())
  stairs = [0]*300
  for i in range(n):
    stairs[i]=int(sys.stdin.readline())

  lst = [0]*300
  lst[0]= stairs[0]
  lst[1]= stairs[0] + stairs[1]
  lst[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2] )
  for i in range(3, n):
    xoo = lst[i-3]+stairs[i-1]+stairs[i]
    oxo = lst[i-2]+stairs[i]
    lst[i]= max(xoo, oxo)
  print(lst[n-1])

sol()