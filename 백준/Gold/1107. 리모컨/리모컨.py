import sys

input = sys.stdin.readline

INF = 2e10
n = int(input())
number_of_errors = int(input())
# errors = sorted(list(map(int, input().split())))
e = [False] * 10
if number_of_errors != 0:
    for value in list(map(int, input().split())):
        e[value] = True
'''
0
9
0 2 3 4 5 6 7 8 9
'''

min_ = INF

# 작은데로 내려가기


def down(start):
    global min_
    tmp = start
    while True:
        if tmp == -1:
            return
        tmp_s = str(tmp)
        cnt = 0
        for c in tmp_s:
            if e[int(c)] == False:
                cnt += 1
        if cnt == len(tmp_s):
            min_ = min(min_, len(tmp_s) + (start - tmp))
            return
        tmp -= 1


# 큰데로 올라가기
def up(start):
    global min_
    tmp = start
    while True:
        if tmp == 1000001:
            return
        tmp_s = str(tmp)
        cnt = 0
        for c in tmp_s:
            if e[int(c)] == False:
                cnt += 1
        if cnt == len(tmp_s):
            min_ = min(min_, len(tmp_s) + (tmp - start))
            return
        tmp += 1


down(n)
up(n)

print(min(min_, abs(100 - n)))
