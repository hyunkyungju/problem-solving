import sys

input = sys.stdin.readline

ips = list(map(int, input().split()))

s = 0
for i in range(5):
  s += pow(ips[i], 2)

print(s % 10)