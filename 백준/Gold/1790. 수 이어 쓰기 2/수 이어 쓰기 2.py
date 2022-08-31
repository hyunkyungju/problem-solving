import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d = 0
nk = k
while nk > 0:
  k = nk
  d += 1
  nk = k - 9 * pow(10, d-1) * d

k -= 1
mok = k // d
namozi = k % d
number = mok + pow(10, d-1)
if number > n:
  print(-1)
  exit()
number_s = str(number)
ans = number_s[namozi]
print(ans)