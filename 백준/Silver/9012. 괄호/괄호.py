import sys

input = sys.stdin.readline

class Stack:
  def __init__(self):
    self.st = list()

  def push(self, x):
    self.st.append(x)

  def pop(self):
    if len(self.st) ==0:
      return ")"
    return self.st.pop()

  def is_empty(self):
    return len(self.st) ==0

def check_vps(str):
  ps = list(str)
  st = Stack()
  for p in ps:
    if p=="(":
      st.push("(")
    elif p==")":
      return_value = st.pop()
      if return_value != "(":
        print("NO")  
        return
  if st.is_empty(): print("YES")
  else: print("NO")

n = int(input())

for _ in range(n):
  check_vps(input())