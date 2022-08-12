import sys
import itertools

input = sys.stdin.readline

n = int(input())
ips = [[0] * (n + 1) for i in range(n + 1)]
tmp = list(input().rstrip())
cnt = 0
for i in range(1, n + 1):
    for j in range(i, n + 1):
        ips[i][j] = tmp[cnt]
        cnt += 1


def bt(s, l):
    if len(s) == n:
        print(*s)
        exit()
    valid = [True] * 21
    asum_minus = sum(s) * -1
    for i in range(1, l + 1):
        sign = ips[i][l]
        if sign == '+':
            for j in range(-10, 11):
              if j <= asum_minus:
                valid[j+10] = False
        elif sign == '-':
            for j in range(-10, 11):
              if j >= asum_minus:
                valid[j+10] = False
        else:
            for j in range(-10, 11):
              if j!=asum_minus:
                valid[j+10] = False
        if i!=l:
          asum_minus += s[i-1]
      
    
    for i in range(0, 21):
        if valid[i]:
            bt(s + [i-10], l+1)



bt([], 1)
