tree = []

def sol():
  global tree
  n, m, k = map(int, input().split())
  tree = [0]*(2*n)
  for i in range(n, 2*n):
    tree[i] = int(input())
  for i in range(n-1, 0, -1):
    tree[i] = tree[2*i] + tree[2*i + 1]
  for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
      update(b-1, c, n)
    else:
      get_sum(b-1, c, n)

def update(idx, num, n):
  idx += n
  before_num = tree[idx]
  change = num - before_num
  tree[idx] = num 
  while idx > 1:
    idx //= 2
    tree[idx] += change

def get_sum(left, right, n):
  ans = 0
  left += n
  right += n 
  while left < right:
    if left % 2 == 1:
      ans += tree[left]
      left += 1
    if right % 2 == 1:
      ans += tree[right-1]
      right -= 1
    left //= 2
    right //= 2
  print(ans)

sol()