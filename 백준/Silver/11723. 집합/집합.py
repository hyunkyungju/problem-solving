import sys
import itertools

input = sys.stdin.readline

t = int(input())
s = [False] * 21
for _ in range(t):
    c = input().split()
    command = c[0]
    x = int(c[1]) if len(c) == 2 else 0
    if command == "add":
        s[x] = True
    elif command == "remove":
        s[x] = False
    elif command == "check":
        print(int(s[x]))
    elif command == "toggle":
        s[x] = not s[x]
    elif command == "all":
        s = [True] * 21
    elif command == "empty":
        s = [False] * 21
