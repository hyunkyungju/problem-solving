import sys
input = sys.stdin.readline

n = int(input())
sol = -1
three_bag_nums = [0, 2, 4, 1, 3]
r = n % 5
n -= three_bag_nums[r] * 3 

if n >= 0:
  sol = three_bag_nums[r] + n//5
print(sol)