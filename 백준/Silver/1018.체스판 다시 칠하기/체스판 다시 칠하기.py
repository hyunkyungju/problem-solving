# 다시 칠해야 하는 정사각형의 최소 개수 구하기
def calculate(table, x, y):
  count = 0
  for i in range(8):
    for j in range(8):
      isEven = (i+j)%2==0
      if isEven and table[x+i][y+j]=='W':
        count += 1
      elif (not isEven) and table[x+i][y+j]=='B':
        count += 1     
  return count            


n, m = map(int, input().split(' '))
table = list()
for i in range(n):
  table.append(list(input()))

white = [['W', 'B']*4, ['B', 'W']*4]*4
black = [['B', 'W']*4, ['W', 'B']*4]*4


minimum = n*m
x, y = 0, 0
for x in range(n-8+1):
  for y in range(m-8+1):
    whitePrice = calculate(table, x, y)
    blackPrice = 64 - whitePrice
    minimum = min(minimum,whitePrice, blackPrice)

print(minimum)

#58m 26s