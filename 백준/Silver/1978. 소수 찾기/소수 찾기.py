import sys
import math

input = sys.stdin.readline


n = int(input())
lst = list(map(int, input().split()))

max = math.sqrt(1000)
prime = 2
primes = list()
numbers = [i for i in range(0, 1001)]
while prime<max:
  i = 2
  while prime * i<1001:
    numbers[prime * i] = -1
    i +=1
  for j in range(prime+1, 1001):
    if numbers[j]!=-1:
      prime = j
      break

cnt = 0
for value in lst:
  if numbers[value] >1:
    cnt +=1
print(cnt)
  


  