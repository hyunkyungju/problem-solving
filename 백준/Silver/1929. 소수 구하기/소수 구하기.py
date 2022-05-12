import sys
import math

input = sys.stdin.readline

m, n = map(int, input().split())

max = math.sqrt(n)
prime = 2
primes = list()
numbers = [i for i in range(0, n+1)]
while prime<=max:
  i = 2
  while prime * i<n+1:
    numbers[prime * i] = -1
    i +=1
  for j in range(prime+1, n+1):
    if numbers[j]!=-1:
      prime = j
      break

for i in range(m, n+1):
  if numbers[i] >1:
    print(i)
