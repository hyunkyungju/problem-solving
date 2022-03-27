import sys

input = sys.stdin.readline

class Stack:
  def __init__(self):
    self.st = list()

  def push(self, x, outputs):
    self.st.append(x)
    outputs.append("+")

  def pop(self, outputs):
    outputs.append("-")
    return self.st.pop()

  def top(self):
    if len(self.st) !=0:
      return self.st[-1]

def func():
  n = int(input())
  outputs = list()
  current = 1
  st = Stack()
  for _ in range(n):
    number = int(input())
    if st.top() == number:
      st.pop(outputs)
    elif current > n or current > number:
      print("NO")
      return
    else:
      while(current <= n and current!=number):
        st.push(current, outputs)
        current +=1
      st.push(current-1, outputs)
      current +=1
      st.pop(outputs)
  
  for output in outputs:
    print(output) 

func()