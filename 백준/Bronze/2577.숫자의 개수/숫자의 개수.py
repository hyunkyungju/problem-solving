
lst = [0]*10
result = 1
for _ in range(3):
  result *=int(input())
result_str = str(result)

for char in result_str:
  n = int(char)
  lst[n] +=1

for n in lst:
  print(n)
