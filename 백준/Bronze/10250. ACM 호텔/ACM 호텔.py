import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    floor = n % h if n % h else h
    walk = (n-1) // h + 1
    print(floor * 100 + walk)
