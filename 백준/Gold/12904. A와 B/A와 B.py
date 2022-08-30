import sys

input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

len_t = len(t)
for i in range(len_t-1, -1, -1):
  if len(s) == len(t):
    if s == t:
      print(1)
    else:
      print(0)
    exit()
  if t[i] == 'A':
    t = t[:-1]
  else:
    t = t[:-1]
    t = t[::-1]