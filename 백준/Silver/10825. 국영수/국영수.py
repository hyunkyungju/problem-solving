import sys
input = sys.stdin.readline

n = int(input())
ips = list()
for _ in range(n):
  name, kor, eng, math =  input().split()
  ips.append((name, int(kor), int(eng), int(math)))
ips.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in ips:
  print(i[0])
