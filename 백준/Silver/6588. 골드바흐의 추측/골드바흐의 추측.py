import sys
import math

input = sys.stdin.readline

max_ = 1000000
prime = 2
primes = list()
numbers = [i for i in range(0, max_+1)]
sqrt_max = math.sqrt(max_)
while prime<=sqrt_max:
  for i in range(2, max_//prime+1):
    numbers[prime * i] = 0
  for j in range(prime+1, max_+1):
    if numbers[j]:
      prime = j
      break
lst = list()

while True:
  n = int(input())
  if not n:
    break
  lst.append(n)

result = [(0, 0)]*len(lst)

for i in range(len(lst)):
  value = lst[i]
  lidx = 2
  ridx = value
  while True:
    if lidx > ridx:
      break
    sum = numbers[lidx] + numbers[ridx]
    if not numbers[lidx]:
      lidx+=1
    elif not numbers[ridx]:
      ridx -=1
    elif sum < value:
      lidx+=1
    elif sum > value:
      ridx -=1
    elif sum == value:
      result[i]=(lidx, ridx)
      break

for a, b in result:
  if a+b:
    print(f"{a+b} = {a} + {b}")
  else:
    print("Goldbach's conjecture is wrong.")

