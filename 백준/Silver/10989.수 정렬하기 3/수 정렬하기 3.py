import sys
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

n = int(input())
lst = [0]*10001
for _ in range(n):
  lst[int(sys.stdin.readline())] += 1
for i in range(len(lst)):
  for _ in range(lst[i]):
    sys.stdout.write(str(i)+"\n")