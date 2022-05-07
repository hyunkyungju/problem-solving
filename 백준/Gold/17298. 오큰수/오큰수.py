import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().rstrip().split()))
result = [-1]*n
stack = list()

for i in range(n):
  value = lst[i]
  while stack and stack[-1][1]<value:
    index, _ = stack.pop()
    result[index] = value
  stack.append((i, value))
  
print(' '.join(map(str, result)))