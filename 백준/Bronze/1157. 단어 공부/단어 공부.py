import sys

input = sys.stdin.readline

s = list(input().rstrip())
lst = [0]*26
for c in s:
  if c.isupper():
    lst[ord(c)-65] +=1
  else:
    lst[ord(c)-97] +=1

max_ = 0
ans = 0
for i in range(len(lst)):
  if lst[i]>max_:
    ans = i
    max_ = lst[i]
  elif lst[i]==max_:
    ans = -2
print(chr(ans+65))