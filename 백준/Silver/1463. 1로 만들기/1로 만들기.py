import sys
import collections
input = sys.stdin.readline

def calculate(tmp):
  if tmp<=n and lst[tmp] ==-1:
    dq.append(tmp)
    lst[tmp] = cnt + 1

n = int(input())

lst = [-1] * (n+1)
dq = collections.deque()
x = 1
lst[1] = 0
while True:
  if x==n:
    print(lst[x])
    break
  cnt = lst[x] 
  calculate(x*3)
  calculate(x*2)
  calculate(x+1)
  x = dq.popleft()
