import sys

input = sys.stdin.readline

r = 31
m = 1234567891
n = int(input())
ips = input().rstrip()
h = 0
for i in range(n): 
  h += (ord(ips[i]) - 96) * pow(r, i) 
  h %= m
print(h)