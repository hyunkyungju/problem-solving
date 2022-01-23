h, m = map(int, input().split())

result = h*60+m
result -=45
if result<0:
  result +=60*24

print(result//60, result%60)