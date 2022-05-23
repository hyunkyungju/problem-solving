import sys

input = sys.stdin.readline

n = int(input())
b = -2
r = 0
lst = list()
while n!=1 and n!=0:
  r = n % abs(b)
  n -= r
  n //= b
  lst.append(r)
lst.append(n)
print(''.join(map(str, reversed(lst))))
