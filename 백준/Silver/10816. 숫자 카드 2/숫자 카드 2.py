import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

card_dict = {}
for card in cards:
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

card_set = sorted(list(set(cards)))
n = len(card_set)

m = int(input())
nums = list(map(int, input().split()))
for i, num in enumerate(nums):
    nums[i] = (i, num)
nums.sort(key=lambda x: x[1])
lst = [0] * m

card_i = 0

for i, value in nums:
    while True and card_i < n:
        if card_set[card_i] == value:
            lst[i] = card_dict[value]
            break
        elif card_set[card_i] > value:
            break
        else:
            card_i += 1

print(*lst)
