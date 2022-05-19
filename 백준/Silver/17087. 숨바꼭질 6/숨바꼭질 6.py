import sys
import math

input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))
ans = abs(lst[0]-s)
for value in lst:
  ans = math.gcd(ans, abs(value-s))

print(ans)