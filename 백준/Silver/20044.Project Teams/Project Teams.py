n = int(input())
student_num = n*2
lst = list(map(int, input().split()))
lst.sort()
teams = [0]*n
for i in range(n):
  teams[i]=lst[i]+lst[student_num-1-i]
print(min(teams))