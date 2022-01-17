# 캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 시작했다. 강산이가 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)
lst = list()
while True:
  n = input()
  if n=="0 0 0":
    break
  else:
    lst.append(list(map(int, n.split(' '))))


for i in range(len(lst)):
  count = (lst[i][2] // lst[i][1]) * lst[i][0]
  count += min(lst[i][2] % lst[i][1], lst[i][0])
  print("Case "+str(i+1)+": "+str(count))

# 13m 20s