import sys
import math

input = sys.stdin.readline

def cal(n, d):
  cnt = 0
  while n:
    n //=d
    cnt +=n
  return cnt
  
n, m = map(int, input().split())  
five = cal(n, 5) - cal(m, 5) - cal(n-m, 5)
two = cal(n, 2) - cal(m, 2) - cal(n-m, 2)
print(min(five, two))