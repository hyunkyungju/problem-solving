import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a_list = list(map(int, input().split()))

for num in a_list:
  if num <x :
    print(num, end=' ')