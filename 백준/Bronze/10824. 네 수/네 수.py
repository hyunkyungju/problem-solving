import sys

input = sys.stdin.readline

lst = input().split()

AB = lst[0]+lst[1]
CD = lst[2]+lst[3]

print(int(AB)+int(CD))