import sys

input = sys.stdin.readline

ips = list(map(int, input().split()))


def ascending():
  for i in range(1, 8):
    if ips[i] != i + 1:   
      return
  print("ascending")
  exit()

def descending():
  for i in range(1, 8): 
    if ips[i] != 8 - i:   
      return
  print("descending")
  exit()


if ips[0] == 1:
  ascending()
      
elif ips[0] == 8:
  descending()

print("mixed")