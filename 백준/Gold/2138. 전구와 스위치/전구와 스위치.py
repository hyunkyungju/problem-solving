import sys

input = sys.stdin.readline


n = int(input())
a = list(map(int, list(input().rstrip())))
b = list(map(int, list(input().rstrip())))

def toggle(lst, i):
  for j in range(3):
      lst[i + j] = int(not lst[i + j])





def sol(lst):
  cnt = 0
  for i in range(n-2):
    if lst[i] != b[i]:
      toggle(lst, i)
      cnt += 1
  if lst[n-2] != b[n-2]:
    lst[n-2] = int(not lst[n-2])
    lst[n-1] = int(not lst[n-1])
    cnt += 1
  if lst == b:
    return cnt
  return -1 

# n-1 처리

# 가장 앞 전등을 켰을 때
ips = a[:]
ips[0] = int(not ips[0])
ips[1] = int(not ips[1])

f_cnt = sol(ips)
if f_cnt != -1:
  f_cnt += 1
  
# 가장 앞 전등을 안 켰을 때
s_cnt = sol(a)
if f_cnt == -1 and s_cnt == -1:
  print(-1)
elif f_cnt == -1:
  print(s_cnt)
elif s_cnt == -1:
  print(f_cnt)
else:
  print(min(s_cnt, f_cnt))

