import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))
lst = [0] * n
sum = 0 
for i, num in enumerate(numbers):
  sum = max(0, sum+num)
  lst[i] = sum 
if max(lst)==0:
  print(max(numbers))
else:
  print(max(lst))