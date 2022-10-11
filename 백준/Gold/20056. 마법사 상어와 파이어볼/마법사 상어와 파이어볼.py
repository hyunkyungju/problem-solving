
n, m, k = map(int, input().split())
table = [[[] for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    ri, ci, mi, si, di = map(int, input().split())
    table[ri][ci].append((mi, si, di))


def move():
    global table
    tmp_table = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    for r in range(1, n+1):
        for c in range(1, n+1):
            lst = table[r][c]
            for mi, si, di in lst:
                nr = r + dr[di]*si
                nc = c + dc[di]*si
                nr = (nr-1) % n + 1
                nc = (nc-1) % n + 1
                tmp_table[nr][nc].append((mi, si, di))
    table = tmp_table





def second_work():
    for r in range(1, n+1):
        for c in range(1, n+1):
            lst = table[r][c]
            if len(lst) <= 1:
                continue
            msum = 0
            ssum = 0
            dir = [0] * len(lst)
            for i, (mi, si, di) in enumerate(lst):
                msum += mi
                ssum += si
                dir[i] = di%2
            table[r][c] = []
            mass = msum // 5
            if not mass:
                continue
            speed = ssum // len(lst)
            dstart = 1
            if sum(dir) == 0 or sum(dir) == len(lst):
                dstart = 0
            for i in range(4):
                table[r][c].append((mass, speed, dstart + i*2))








for _ in range(k):

    # 1. 이동
    move()

    # 2. 파이어볼
    second_work()

ans = 0
for r in range(1, n+1):
    for c in range(1, n+1):
        for m, _, _ in table[r][c]:
            ans += m
print(ans)