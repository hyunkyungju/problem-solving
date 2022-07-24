import sys
import math

input = sys.stdin.readline

n = int(input())
n_sqrt = int(math.sqrt(n))

# n의 제곱근(n_sqrt)보다 작거나 같은 소수들을 찾아야함
is_prime = [True] * (n_sqrt + 1)
for i in range(2, int(math.sqrt(n_sqrt)) + 1):
    for j in range(2, n_sqrt // i + 1):
        is_prime[i * j] = False

tmp = 2
while (n >= n_sqrt +1 or not is_prime[n]) and tmp<n_sqrt+1:
    if is_prime[tmp] and not n % tmp:
        print(tmp)
        n = n // tmp
    else:
        tmp += 1
      
if n!=1: print(n)
  