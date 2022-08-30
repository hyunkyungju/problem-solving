import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
nums = list(map(int, input().split()))
for i, num in enumerate(nums):
  nums[i] = (i, num)
nums.sort(key=lambda x:x[1])
lst = [0] * m



card_i = 0

for i, value in nums:
  while True and card_i < n:
    if cards[card_i] == value:
      lst[i] = 1
      break
    elif cards[card_i] > value:
      break
    else:
      card_i += 1

print(*lst)
    