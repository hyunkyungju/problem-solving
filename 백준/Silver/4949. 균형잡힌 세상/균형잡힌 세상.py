import sys
input = sys.stdin.readline

def is_balanced(s):
  st = list()
  for c in s:
    if c == "(":
      st.append(c)
    elif c == ")":
      if not len(st) or st.pop() != "(":
        return False
    elif c == "[":
      st.append(c)
    elif c == "]":
      if not len(st) or st.pop() != "[":
        return False      
  if len(st):
    return False
  return True
  
while True:
  s = input().rstrip()
  if s == ".":
    exit()
  if is_balanced(s):
    print("yes")
  else:
    print("no")