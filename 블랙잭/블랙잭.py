# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

n, m = map(int, input().split(' '))
cards = list(map(int, input().split(' '))) # str list -> int list

max = 0
for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      value = cards[i]+cards[j]+cards[k]
      if max < value and value<=m:
        max = value
print(max)

# 6m 42s