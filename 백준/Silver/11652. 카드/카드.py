import sys
input = sys.stdin.readline

n = int(input())
ips = list()
for _ in range(n):
  ips.append(int(input()))
ips.sort()

if n == 1:
  print(ips[0])
  exit()

lst = list()
cnt = 1
i = 0
while i < n - 1:
  if ips[i] == ips[i+1]:
    cnt += 1
  else:
    lst.append((ips[i], cnt))
    cnt = 1
  i += 1
  
lst.append((ips[-1], cnt))
ans = min(lst, key = lambda x : -x[1])
print(ans[0])