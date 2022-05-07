import sys

input = sys.stdin.readline

lst = input().rstrip()

result=""
stack = list()
priority = {"+":1, "-":1, 
        "*":0, "/":0, "(":2}

for c in lst:
  if c =='(':
    stack.append(c)
  elif c==')':
    while stack and stack[-1]!='(':
      result += stack.pop()
    stack.pop()
  elif c in priority:
    while stack and priority.get(stack[-1])<=priority.get(c):
      result += stack.pop()
    stack.append(c)
  else:
    result +=c
while stack:
  result += stack.pop()
result = result.replace('(', '')
result = result.replace(')', '')
print(result)