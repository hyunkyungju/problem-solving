import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))
maxes = [0, numbers[0]]
roads = [0, maxes[1:]]

for number in numbers:
  for cnt, max_ in enumerate(maxes):
    if max_>number:
      if maxes[cnt-1] < number:
        maxes[cnt] = number
        roads[cnt][cnt-1] = number
        roads[cnt] = maxes[1:cnt+1]  
      break
  if max(maxes)<number:
    maxes.append(number)
    tmp = roads[-1][:]
    tmp.append(number)
    roads.append(tmp)

maxes.pop(0)
print(len(maxes))
# print(' '.join(map(str, roads[len(maxes)])))
'''
6
1 3 5 7 2 3
'''