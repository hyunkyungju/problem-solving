import sys

input = sys.stdin.readline

s = input().rstrip()
lst = [0]*26
for c in s:
  lst[ord(c)-97] +=1

print(' '.join(map(str, lst)))
