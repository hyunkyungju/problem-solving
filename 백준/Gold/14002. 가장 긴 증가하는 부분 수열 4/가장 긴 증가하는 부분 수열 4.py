import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))
maxes = [0, numbers[0]]
roads = [[], maxes[1:]]

for number in numbers:
  for cnt, max_ in enumerate(maxes):
    if max_>number:
      if maxes[cnt-1] < number:
        maxes[cnt] = number
        tmp = roads[cnt-1][:]
        tmp.append(number)
        roads[cnt] = tmp  
      break
  if max(maxes)<number:
    maxes.append(number)
    tmp = roads[-1][:]
    tmp.append(number)
    roads.append(tmp)


maxes.pop(0)
print(len(maxes))
print(' '.join(map(str, roads[len(maxes)])))
