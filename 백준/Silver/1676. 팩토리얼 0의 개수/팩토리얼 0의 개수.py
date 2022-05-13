import sys
import math

input = sys.stdin.readline

def cal():
  fac = math.factorial(int(input()))
  s = str(fac)[::-1]
  for i in range(len(s)):
    c = s[i]
    if c!="0":
      print(i)
      return
cal()