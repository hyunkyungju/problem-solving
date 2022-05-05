import sys
from collections import deque

input = sys.stdin.readline


class Deque():
  def __init__(self):
    self.dq = deque()
    

  def push_front(self, x):
    self.dq.appendleft(x)
    
  def push_back(self, x): 
    self.dq.append(x)
    
  def pop_front(self):
    if self.dq:
      return self.dq.popleft()
    return -1
    
  def pop_back(self):
    if self.dq:
      return self.dq.pop()
    return -1

  def size(self):
    return len(self.dq) 
    
  def empty(self):    
    if self.dq:
      return 0
    return 1

  def front(self):
    if self.dq:
      return self.dq[0]
    return -1
    
  def back(self):
    if self.dq:
      return self.dq[-1]
    return -1

deque = Deque()


command_runner = {"push_front": lambda dq, x: dq.push_front(x),
                  "push_back": lambda dq, x: dq.push_back(x),
                  "pop_front": lambda dq: dq.pop_front(),
                  "pop_back": lambda dq: dq.pop_back(),
                  "size": lambda dq: dq.size(),
                  "empty": lambda dq: dq.empty(),
                  "front": lambda dq: dq.front(),
                  "back": lambda dq: dq.back()
                 } 

n = int(input())
for _ in range(n):
  commands = input().rstrip().split(' ')
  if len(commands)==2:
    (command_runner.get(commands[0]))(deque, commands[1])
  else:
    print((command_runner.get(commands[0]))(deque))
      
  

