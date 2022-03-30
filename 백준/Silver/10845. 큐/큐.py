class queue:
  def __init__(self):
    self.removed = 0
    self.queue = list()

  def empty_handle(self):
    if not self.get_size(): 
      print(-1)    
      return True
    return False
  
  def push(self, x):
    self.queue.append(x)

  def pop(self):
    if not self.empty_handle():
      self.removed += 1
      print(self.queue[self.removed-1])
    
  def size(self):
    print(self.get_size())

  def get_size(self):
    return len(self.queue)-self.removed

  def empty(self):
    if not self.get_size():
      print(1)
      return
    print(0)

  def front(self):
   if not self.empty_handle():    
    print(self.queue[self.removed])

  def back(self):
    if not self.empty_handle():
      print(self.queue[-1])
      

import sys

input = sys.stdin.readline

n = int(input())
q = queue()
for _ in range(n):
  commands = input().split()
  if commands[0]=="push":
    q.push(commands[1])
  elif commands[0]=="pop":
    q.pop()
  elif commands[0]=="size":
    q.size()
  elif commands[0]=="empty":
    q.empty()
  elif commands[0]=="front":
    q.front()
  else:
    q.back()
