import sys

input = sys.stdin.readline

for s in sys.stdin:
  lower = 0
  upper = 0
  digit = 0
  blank = 0
  for c in s:
    if c.islower():
      lower +=1
    elif c.isupper():
      upper +=1
    elif c.isdigit():
      digit +=1
    elif c==' ':
      blank +=1
  print(lower, upper, digit, blank)
  

