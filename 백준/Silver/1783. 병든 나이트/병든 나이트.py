import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ans = 0
if n == 1:
  ans = 1
elif n == 2:
  ans = min((m-1)//2+1, 4)
elif m <= 6:
  ans = min(m, 4)
else:
  ans = m-2

print(ans)