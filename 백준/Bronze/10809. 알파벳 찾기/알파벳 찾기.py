import sys

input = sys.stdin.readline

s = input().rstrip()
lst = [-1]*26
for i in range(len(s)):
  if lst[ord(s[i])-97] == -1:
    lst[ord(s[i])-97] = i

print(' '.join(map(str, lst)))
