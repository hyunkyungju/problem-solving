import sys
n = int(sys.stdin.readline())
st = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

for i in x:
  if i in st:
    print(1)
  else:
    print(0)
