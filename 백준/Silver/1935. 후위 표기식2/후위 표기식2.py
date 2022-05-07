import sys

input = sys.stdin.readline

n = int(input())
lst = input().rstrip()
operands = list()
for i in range(n):
  operands.append(int(input()))
  


stack = list()
dict = {"+":lambda x, y: y+x, 
        "-":lambda x, y: y-x, 
        "*":lambda x, y: y*x, 
        "/":lambda x, y: y/x}

for c in lst:
  if c in dict:
    stack.append((dict.get(c))(stack.pop(), stack.pop()))
  else:
    stack.append(operands[ord(c)-65])
print("{:.2f}".format(stack.pop()))