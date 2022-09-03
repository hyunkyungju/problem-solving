import sys

input = sys.stdin.readline

n = int(input())
ips = []
for _ in range(n):
    ips.append(input().rstrip())
ips.sort(key=lambda x: (len(x), x))
new_lst = []
for i in ips:
    if i in new_lst:
      continue
    print(i)
    new_lst.append(i)