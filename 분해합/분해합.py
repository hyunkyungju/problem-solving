# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

n = int(input())

result = 0
for i in range(n):
  if (sum(map(int, str(i)))+i) == n:
    result = i
    break
print(result)

# 6m 28s 