import sys
input = sys.stdin.readline

n = int(input())
ps = []
num_zero = 0
ns = []
ans = 0
for _ in range(n):
  value = int(input())
  if value > 1:
    ps.append(value)
  elif value == 1:
    ans += 1
  elif value == 0:
    num_zero += 1
  else:
    ns.append(value)
ps.sort(reverse=True)
ns.sort()

def combine(lst):
  global ans
  for i in range(0, len(lst) -1 , 2):
    ans += lst[i] * lst[i+1]

combine(ps)
if len(ps) % 2 == 1:
  ans += ps[-1]

combine(ns)
if len(ns) % 2 == 1 and not num_zero:
  ans += ns[-1]
    
print(ans)