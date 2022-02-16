c = int(input())

for _ in range(c):
  lst = list(map(int, input().split()))
  n = lst[0]
  del lst[0]
  avg = sum(lst)/n
  cnt = 0
  for student in lst:
    if student > avg:
      cnt +=1
  print("{:.3f}%".format(cnt/n * 100))
