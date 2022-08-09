import sys
input = sys.stdin.readline

se, ss, sm = map(int, input().split())

e, s, m = 1, 1, 1

y = 1
while True:
  if e==se and s == ss and m == sm:
    print(y)
    break
  e = e + 1 if e!=15 else 1
  s = s + 1 if s!=28 else 1
  m = m + 1 if m!=19 else 1
  y +=1
