import sys

input = sys.stdin.readline


n = int(input())
ips = {}
for _ in range(n):
  v, l, r = input().split()
  ips[v] = l, r


def print_(s):
  print(s, end='')

def pre(p):
  print_(p)
  l, r = ips[p]
  if l != '.':
    pre(l)
  if r != '.':
    pre(r)    

def in_(p):
  l, r = ips[p]
  if l != '.':
    in_(l)
  print_(p)
  if r != '.':
    in_(r)

def post(p):
  l, r = ips[p]
  if l != '.':
    post(l)
  if r != '.':
    post(r)    
  print_(p)
    

root = 'A'
pre(root)
print()
in_(root)
print()
post(root)

