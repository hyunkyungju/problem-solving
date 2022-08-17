import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, 1, -1, 1, -1, 1, -1]
w, h = 0, 0
ips = list()

def dfs(row, col):
  for i in range(8):
    nr = row + dr[i]
    nc = col + dc[i]
    if nr < 0 or nr >= h or nc < 0 or nc >= w:
      continue
    if ips[nr][nc] == 1:
      ips[nr][nc] = 0
      dfs(nr, nc)

while True:
  cnt = 0
  w, h = map(int, input().split())
  if not w and not h:
    break
  ips = [list(map(int, input().split())) for _ in range(h)]
  for row in range(h):
    for col in range(w):
      if ips[row][col] == 1:
        dfs(row, col)
        cnt += 1
  print(cnt)
