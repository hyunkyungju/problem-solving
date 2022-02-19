lst = [0]*10001

def d(n):
  digit_sum = sum(list(map(int, str(n))))
  if n + digit_sum <=10000:
    lst[n+digit_sum] = 1

for i in range(10000):
  d(i)

for i in range(10001):
  if lst[i] == 0:
    print(i)