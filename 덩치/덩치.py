n = int(input())
lst = list()
for i in range(n):
  lst.append(list(map(int, input().split(' '))))

result=[1]*n
for i in range(n):
  for j in range(i+1, n):
    if lst[i][0]>lst[j][0] and lst[i][1]>lst[j][1]:
      result[j] +=1
    elif lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
      result[i] +=1
  

for r in result:
  print(r, end=' ')

# 15m 49s 