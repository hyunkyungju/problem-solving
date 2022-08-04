import sys

input = sys.stdin.readline

n = int(input())
inputs = list(map(int, input().split()))
lst = [0]*(max(inputs)+1)
for number in inputs:
  lst[number] = max(lst[0:number])+number
print(max(lst))