import sys

input = sys.stdin.readline

def is_palindrome(s):
  len_ = len(s)
  for i in range(len_ // 2):
    if s[i] != s[len_-1-i]:
      return False
  return True

while True:
  str = input().rstrip()
  if str == '0':
    exit()
  if is_palindrome(str):
    print("yes")
  else:
    print("no")


  