import sys

input = sys.stdin.readline

n = int(input())
ips = {}
for _ in range(n):
    v, l, r = map(int, input().split())
    ips[v] = l, r

# get root
is_root = [True] * (n+1)
is_root[0] = False
for l, r in ips.values():
  if l  != -1:
    is_root[l] = False
  if r != -1:
    is_root[r] = False


root = is_root.index(True)

# get depth
d = 1
def get_d(v, level):
    global d
    d = max(d, level)
    l, r = ips[v]
    if l != -1:
        get_d(l, level + 1)
    if r != -1:
        get_d(r, level + 1)
get_d(root, 1)

# make the table
t = [[-1] * n for _ in range(d)]
col = 0

def inorder(v, level):
  global col
  l, r = ips[v]
  if l != -1:
    inorder(l, level + 1)
  t[level][col] = v
  col += 1
  if r != -1:
    inorder(r, level + 1)

inorder(root, 0)

# find the max diff
depth_at_max = 0
max_width = 0

for i in range(d-1, -1, -1):
  l, r = 0, 0
  for j in range(n):
    if t[i][j] != -1:
      l = j
      break
  for j in range(n-1, -1, -1):
    if t[i][j] != -1:
      r = j
      break
  diff_width = r - l
  if diff_width >= max_width:
    max_width = diff_width
    depth_at_max = i

print(depth_at_max + 1, max_width + 1)