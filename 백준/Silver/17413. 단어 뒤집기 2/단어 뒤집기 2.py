import sys

input = sys.stdin.readline

s = input().rstrip()

a = s.replace('>','<').split('<')

result = ""
for i in range(len(a)):
  if i%2: 
    result += '<'+a[i]+'>'
  else:
    c = a[i].split()
    result+=' '.join([d[::-1] for d in c])

print(result)