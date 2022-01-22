import sys
def calculate(cookie,n, x, y, a, b):
  result=0
  while 0 <= x+a*(result+1) and  x+a*(result+1)<n and 0<= y+b*(result+1) and y+b*(result+1)<n:
    if cookie[x+a*(result+1)][y+b*(result+1)]=='*':
      result+=1
    else:
      break
  return result

n=int(input())
cookie=list()
for _ in range (n):
  cookie.append(list(sys.stdin.readline()))
for i in range(1, n-1):
  for j in range(1, n-1):
    if cookie[i][j]=='*' and cookie[i-1][j]=='*' and cookie[i+1][j]=='*' and cookie[i][j-1]=='*' and cookie[i][j+1]=='*':
      x=i
      y=j
      break

left_arm = calculate(cookie, n, x, y, 0, -1)
right_arm = calculate(cookie, n, x, y, 0, 1)
waist = calculate(cookie, n, x, y, 1, 0)
left_leg = calculate(cookie, n, x+waist, y-1, 1, 0)
right_leg = calculate(cookie, n, x+waist, y+1, 1, 0)

print(x+1, y+1)
print(left_arm, right_arm, waist, left_leg, right_leg)

