import sys
input = sys.stdin.readline

n = int(input())
lst = [1]*10
lst[0] = 0

for i in range(n-1):
  tmp = [0]*10
  tmp[0] = lst[1] % 1000000000
  for j in range(1, 9):
    tmp[j] = (lst[j-1] + lst[j+1]) % 1000000000
  tmp[9] = lst[8] % 1000000000
  lst = tmp
print(sum(lst) % 1000000000 )  
    