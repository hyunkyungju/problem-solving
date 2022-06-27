import sys
import math

input = sys.stdin.readline

n, b = input().split()
b = int(b)
number = 0
for i, c in enumerate(list(reversed(n))):
  if c.isalpha():
    tmp = ord(c)-55
  else:
    tmp = int(c)
  number += tmp * pow(b, i)
print(number)