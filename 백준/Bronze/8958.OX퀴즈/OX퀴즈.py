
n = int(input())
for _ in range(n):
  score = 1
  sum = 0
  lst = list(input())
  for ox in lst:
    if ox=="O":
      sum += score
      score +=1
    else:
      score = 1
  print(sum)