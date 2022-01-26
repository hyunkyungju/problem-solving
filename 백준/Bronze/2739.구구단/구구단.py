# 출력형식과 같게 N*1부터 N*9까지 출력한다.

n = int(input())

for i in range(1, 10):
  print(n, '*', i,'=',n*i )