import sys
import itertools

input = sys.stdin.readline


n, m = map(int, input().split())

def bt(s):
  if len(s)==m:
    print(' '.join(map(str, s)))
    return
  for i in range(1, n+1):
    if i not in s:
      bt(s+[i])

bt([])