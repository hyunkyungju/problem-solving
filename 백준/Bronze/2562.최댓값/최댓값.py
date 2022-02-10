
lst = [0] * 9
for i in range(9):
  lst[i]=int(input())

maximum = max(lst)
print(maximum)
print(lst.index(maximum)+1)
