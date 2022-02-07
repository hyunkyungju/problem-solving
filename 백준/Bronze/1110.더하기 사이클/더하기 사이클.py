n = int(input())

start = n
cycle = 0
while True:
  cycle +=1
  h = n //10
  l = n % 10
  added = (h + l) % 10
  new = l * 10 + added
  if start==new:
    print(cycle)
    break
  n = new
