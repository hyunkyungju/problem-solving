import sys

input = sys.stdin.readline

class Stack:
  def __init__(self):
    self.st = list()

  def push(self, x):
    self.st.append(x)

  def pop(self):
    return self.st.pop()

  def top(self):
    return self.st[-1]  

  def size(self):
    return len(self.st)

  def print_all(self):
    while self.size()!=0:
      print(self.pop(),end='')
  
  def clear(self):
    self.st = list()

st = Stack()

str = input().rstrip()
tag_stage = False
tag_start_index = 0
for i in range (len(str)):
  c = str[i]
  if tag_stage: 
    if c=='>':
      while st.top()!='<':
        st.pop()
      st.pop()
      if not st.size():
        for id in range(tag_start_index, i+1):
          print(str[id], end='')
        tag_stage=False
    else:
      st.push(c)

  else:
    if c=='<':
      st.print_all()
      st.clear()
      tag_start_index = i
      tag_stage = True
      st.push(c)
    else:
      if c!=' ':
        st.push(c)
      else:
        st.print_all()
        st.clear()
        print(' ',end='')
st.print_all()
st.clear()