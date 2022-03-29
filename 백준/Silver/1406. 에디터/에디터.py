import sys

input = sys.stdin.readline

lst1 = list(input().rstrip())
lst2 = list()

for _ in range(int(input())):
  command = input().split()
  if command[0]=="L":
    if lst1:
      lst2.append(lst1.pop())
  elif command[0]=="D":
    if lst2:
      lst1.append(lst2.pop())
  elif command[0]=="B":
    if lst1:
      lst1.pop()
  else:
    lst1.append(command[1])

lst1.extend(reversed(lst2))

for item in lst1:
  print(item, end='')



