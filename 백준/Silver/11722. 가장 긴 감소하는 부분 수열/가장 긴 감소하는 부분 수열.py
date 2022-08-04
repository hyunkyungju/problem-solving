import sys

input = sys.stdin.readline

n = int(input())
inputs = list(map(int, input().split()))
max_input = max(inputs)
lst = [0] * (max_input + 2)
for number in inputs:
  lst[number] = max(lst[number+1:]) + 1
print(max(lst))
