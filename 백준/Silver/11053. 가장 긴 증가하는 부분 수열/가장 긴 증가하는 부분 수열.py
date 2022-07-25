import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))
maxes = [0, numbers[0]]
for number in numbers:
  for cnt, max_ in enumerate(maxes):
    if max_>number:
      if maxes[cnt-1] < number:
        maxes[cnt] = number
      break
  if max(maxes)<number:
    maxes.append(number)
print(maxes.index(max(maxes)))
