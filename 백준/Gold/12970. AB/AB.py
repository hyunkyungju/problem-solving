import sys

input = sys.stdin.readline

n, k = map(int, input().split())

a = n // 2
b = n - a
if a * b < k:
  print(-1)
  exit()

b_last = k // a
b_mid_index = k % a
b_zero = b - b_last 
if b_mid_index:
  b_zero -= 1


s = ""
s += "B"*b_zero
for _ in range(b_mid_index):
  s += "A"
if b_mid_index:
  s += "B"
for _ in range(b_mid_index, a):
  s += "A"
s += "B"*b_last
print(s)

