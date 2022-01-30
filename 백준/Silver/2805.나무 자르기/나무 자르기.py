def calculate(lst, h):
  sum=0
  for i in lst:
    if i>h:
      sum += (i-h)
  return sum


import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
result = 0
start = 1
end = 1000000000
while start<=end:
  mid = (start+end)//2
  sum = calculate(lst, mid)
  if sum>=m:
    result = mid
    start = mid +1
  else:
    end = mid-1

print(result)