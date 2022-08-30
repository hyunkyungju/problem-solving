import sys
input = sys.stdin.readline

ips = input().rstrip()
lst = ips.split("-")
ans = 0 
for i, str in enumerate(lst):
  tmp = list(map(int, str.split('+')))
  if not i:
    ans += sum(tmp)
  else:
    ans -= sum(tmp)
print(ans)