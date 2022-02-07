
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def union(a, b):
  a_parent = find_parent(a)
  b_parent = find_parent(b)
  if a_parent >= b_parent:
    parent[a_parent] = b_parent
  else:
    parent[b_parent] = a_parent

def find_parent(a):
  if parent[a] != a:
    parent[a] = find_parent(parent[a])
  return parent[a]

def isSameTeam(a, b):
  if find_parent(a)==find_parent(b):
    print("YES")
  else:
    print("NO")


for _ in range(m):
  command, a, b = map(int, input().split())
  if command == 0:
    union(a, b)
  else:
    isSameTeam(a, b)
