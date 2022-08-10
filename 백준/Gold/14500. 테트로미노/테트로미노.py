import sys

input = sys.stdin.readline

n, m = map(int, input().split())
t = [[0] * m for _ in range(n)]

for i in range(n):
    t[i] = list(map(int, input().split()))

max_ = 0


def blue():
    global max_
    for i in range(n):
        for j in range(m - 3):
            cnt = 0
            for k in range(4):
                cnt += t[i][j + k]
            max_ = max(max_, cnt)

    for i in range(n - 3):
        for j in range(m):
            cnt = 0
            for k in range(4):
                cnt += t[i + k][j]
            max_ = max(max_, cnt)


def yellow():
    global max_
    di = [0, 0, 1, 1]
    dj = [0, 1, 0, 1]
    for i in range(n - 1):
        for j in range(m - 1):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)


def orange():
    global max_
    di = [0, 1, 2, 2]  # i
    dj = [0, 0, 0, 1]  # j
    for i in range(n - 2):
        for j in range(m - 1):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 0, 0, 1]  # i
    dj = [0, 1, 2, 0]  # j
    for i in range(n - 1):
        for j in range(m - 2):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 0, 1, 2]  # i
    dj = [0, 1, 1, 1]  # j
    for i in range(n - 2):
        for j in range(m - 1):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 1, 1, 1]  # i
    dj = [2, 0, 1, 2]  # j
    for i in range(n - 1):
        for j in range(m - 2):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 1, 2, 2]  # i
    dj = [1, 1, 0, 1]  # j
    for i in range(n - 2):
        for j in range(m - 1):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 0, 0, 1]  # i
    dj = [0, 1, 2, 2]  # j
    for i in range(n - 1):
        for j in range(m - 2):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 0, 1, 2]  # i
    dj = [0, 1, 0, 0]  # j
    for i in range(n - 2):
        for j in range(m - 1):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 1, 1, 1]  # i
    dj = [0, 0, 1, 2]  # j
    for i in range(n - 1):
        for j in range(m - 2):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)


def green():
    global max_
    di = [0, 1, 1, 2]  # i
    dj = [0, 0, 1, 1]  # j
    for i in range(n - 2):
        for j in range(m - 1):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 0, 1, 1]  # i
    dj = [1, 2, 0, 1]  # j
    for i in range(n - 1):
        for j in range(m - 2):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 1, 1, 2]  # i
    dj = [1, 1, 0, 0]  # j
    for i in range(n - 2):
        for j in range(m - 1):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 0, 1, 1]  # i
    dj = [0, 1, 1, 2]  # j
    for i in range(n - 1):
        for j in range(m - 2):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)


def purple():
    global max_
    di = [0, 0, 0, 1]  # i
    dj = [0, 1, 2, 1]  # j
    for i in range(n - 1):
        for j in range(m - 2):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 1, 1, 2]  # i
    dj = [1, 0, 1, 1]  # j
    for i in range(n - 2):
        for j in range(m - 1):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 1, 1, 1]  # i
    dj = [1, 0, 1, 2]  # j
    for i in range(n - 1):
        for j in range(m - 2):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)

    di = [0, 1, 1, 2]  # i
    dj = [0, 0, 1, 0]  # j
    for i in range(n - 2):
        for j in range(m - 1):
            cnt = 0
            for k in range(4):
                cnt += t[i + di[k]][j + dj[k]]
            max_ = max(max_, cnt)


blue()
yellow()
orange()
green()
purple()

print(max_)
