import sys

input = sys.stdin.readline

a, b = map(int, input().split())


def cal(a, b):
  cgd = 1
  while True:
    is_change = False
    for i in range(2, min(a, b)+1):
      if a%i==0 and b%i==0:
        a//=i
        b//=i
        cgd*=i
        is_change = True
        break
    if not is_change:
      print(cgd, cgd*a*b, sep='\n')
      return

cal(a, b)
