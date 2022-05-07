import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().rstrip().split()))
result = [-1]*n
stack = list()
count = [0]*(max(lst)+1)

for value in lst:
  count[value] +=1


for i in range(n):
  value = count[lst[i]]
  while stack and stack[-1][1]<value:
    index, _ = stack.pop()
    result[index] = lst[i]
  stack.append((i, value))
  
print(' '.join(map(str, result)))