# 최대 사용할 수 있는 회의의 최대 개수

class Data:
  def __init__(self, start, finish):
    self.start = start
    self.finish = finish
  def __lt__(self, other):
    return (self.finish < other.finish) or (self.finish == other.finish and self.start < other.start)
  def get_start(self):
    return self.start
  def get_finish(self):
    return self.finish

from queue import PriorityQueue

q = PriorityQueue()
n = int(input())
for i in range(n):
  start, finish = map(int, input().split(' '))
  q.put(Data(start, finish))

reserved = 0
result = 0
for i in range(n):
  data = q.get()
  if data.get_start() >=reserved:
    result += 1
    reserved = data.get_finish()

print(result)

#26m 33s