import sys

input = sys.stdin.readline

s = input().rstrip()
lst = list()

for i in range(len(s)):
  lst.append(s[i:])
lst.sort()
print('\n'.join(lst))