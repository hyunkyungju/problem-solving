# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

x, y = map(int, input().split())
print(x+y, x-y, x*y, x//y, x%y, sep='\n')