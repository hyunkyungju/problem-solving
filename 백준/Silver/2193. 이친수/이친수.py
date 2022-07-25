import sys
input = sys.stdin.readline

n = int(input())
zero = 0
one = 1
for i in range(n-1):
  zero_tmp = zero + one
  one = zero
  zero = zero_tmp
print(one+zero)
    