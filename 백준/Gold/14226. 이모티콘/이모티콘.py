import sys
from collections import deque

input = sys.stdin.readline

s = int(input())

q = deque()
q.append((1, 0, 0)) # 현재 임티 수, 클립보드의 임티 수, 레벨 

max_ = 1024
lst = [[-1] * (max_ + 1) for _ in range(max_ + 1)]


def put(e, c, l):
  if e > 1024 or c > 1024 or lst[e][c] != -1:
    return
  lst[e][c] = l
  q.append((e, c, l))

while q:
  e, c, l = q.popleft()
  if e == s:
    print(l)
    break

  # 1. 복사해서 클립보드에 저장
  if e != c:
    put(e, e, l + 1)

  # 2. 임티 화면에 복붙
  if c > 0:
    put(e + c, c, l + 1)

  # 3. 임티 하나 삭제
  if e > 0:
    put(e - 1, c, l + 1)


