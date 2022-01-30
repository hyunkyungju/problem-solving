import sys
n = int(sys.stdin.readline())
red_price=list()
green_price=list()
blue_price=list()

for i in range(n):
  r,g,b=map(int, sys.stdin.readline().split())
  red_price.append(r)
  green_price.append(g)
  blue_price.append(b)

red_result = [0]*n
green_result = [0]*n
blue_result = [0]*n

red_result[0] = red_price[0]
green_result[0] = green_price[0]
blue_result[0] = blue_price[0]

for i in range(1, n):
  red_result[i]= min(green_result[i-1], blue_result[i-1]) + red_price[i]
  green_result[i]= min(red_result[i-1], blue_result[i-1]) + green_price[i]
  blue_result[i]= min(green_result[i-1],red_result[i-1]) + blue_price[i]
print(min(red_result[n-1], green_result[n-1], blue_result[n-1]))