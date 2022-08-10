import sys
import itertools

input = sys.stdin.readline

n = int(input())

def bt(s):
  if len(s)==n:
    print(*s)
    return
  for i in range(1, n+1):
    if i not in s:
      bt(s+[i])
      
bt([])