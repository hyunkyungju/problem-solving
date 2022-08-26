import sys

input = sys.stdin.readline

a, b = input().split()
ar = a[::-1]
br = b[::-1]
print(max(ar, br))