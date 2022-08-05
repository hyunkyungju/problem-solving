import sys

input = sys.stdin.readline

n = int(input())
inputs = list(map(int, input().split()))
max_input = max(inputs)

a = [0] * n
b = [0] * n

inc = [0] * (max_input+2)
dec = [0] * (max_input+2)

for i in range(n):
  value = inputs[i]
  inc[value] = max(inc[0:value])+1 
  a[i] = inc[value] 

  value = inputs[n-1-i]
  dec[value] = max(dec[0:value])+1
  b[n-1-i] = dec[value]

c = [0] * n
for i in range(n):
  c[i] = a[i] + b[i]

print(max(c)-1)