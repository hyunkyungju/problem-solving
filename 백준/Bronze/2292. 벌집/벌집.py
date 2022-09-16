import sys

input = sys.stdin.readline

n = int(input())

cnt = 1
sum_ = 1
while sum_ < n:
  sum_ += cnt * 6
  cnt += 1
print(cnt)