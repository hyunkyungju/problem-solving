import sys
import itertools

input = sys.stdin.readline

k, q, l, b, kn, p = map(int, input().split())
print(1-k, 1-q, 2-l, 2-b, 2-kn, 8-p)

