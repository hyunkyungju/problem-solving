import sys

input = sys.stdin.readline

str = input().rstrip()

left = 0
total = 0
before_left = True
for c in str:
  if c=='(':
    left +=1
    before_left = True

  else:
    if before_left:
      left -= 1
      total += left
    else:
      left -=1
      total +=1
    before_left = False

print(total)