def calculate(lst, mid):
  cnt=0
  for i in lst:
    cnt += i//mid
  return cnt


import sys
k, n = map(int, sys.stdin.readline().split())
lst = list()
for _ in range(k):
  lst.append(int(sys.stdin.readline()))

start = 1
end = max(lst)
while start<=end:
  mid = (start+end)//2
  cnt = calculate(lst, mid)
  if cnt>=n:
    result = mid
    start = mid +1
  else:
    end = mid-1

print(result)