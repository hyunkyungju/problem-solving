
n = int(input())
numbers = list(map(int, input().split()))
maximum = max(numbers)
sum = 0
for number in numbers:
  sum += number/maximum * 100
print(sum/n)