import sys

input = sys.stdin.readline

n = int(input())

lst = list(input().rstrip())
ls = list(map(int, lst))
print(sum(ls))
