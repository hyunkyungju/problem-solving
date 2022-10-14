from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

n, m, k = map(int, input().split())
table = [[0]*(m+1) for _ in range(n+1)]
check_list = []
heaters = []
blocks = [[[False]*4 for _ in range(m+1)] for _ in range(n+1)]


for i in range(n):
    lst = list(map(int, input().split()))
    for j, val in enumerate(lst):
        if not val:
            continue
        elif val == 5:
            check_list.append((i+1, j+1))
        elif val == 1 or val == 4:
            heaters.append((i+1, j+1, val-1))
        elif val == 2:
            heaters.append((i + 1, j + 1, val))
        elif val == 3:
            heaters.append((i + 1, j + 1, 1))

w = int(input())
for _ in range(w):
    x, y, t = map(int, input().split())
    if not t:
        blocks[x][y][1] = True
        blocks[x-1][y][3] = True
    else:
        blocks[x][y][0] = True
        blocks[x][y+1][2] = True


def in_range(nr, nc):
    return 1 <= nr < n+1 and 1 <= nc < m + 1


def put_v(q, is_visited, r, c, num):
    q.append((r, c))
    is_visited[r][c] = True
    table[r][c] += num


def wind():
    for hr, hc, hd in heaters:
        q = deque()
        is_visited = [[False]*(m+1) for _ in range(n+1)]
        nr = hr+dr[hd]
        nc = hc+dc[hd]

        put_v(q, is_visited, nr, nc, 5)

        for num in range(4, 0, -1):
            len_q = len(q)
            for _ in range(len_q):
                vr, vc = q.popleft()
                for idx in [1, 3]:
                    nr = vr + dr[hd] + dr[(hd+idx)%4]
                    nc = vc + dc[hd] + dc[(hd+idx)%4]
                    if in_range(nr, nc) and not is_visited[nr][nc] and not blocks[vr][vc][(hd+idx)%4] and not blocks[nr][nc][(hd+2)%4]:
                        put_v(q, is_visited, nr, nc, num)

                nr = vr + dr[hd]
                nc = vc + dc[hd]
                if in_range(nr, nc) and not is_visited[nr][nc] and not blocks[nr][nc][(hd + 2) % 4]:
                    put_v(q, is_visited, nr, nc, num)




chocolate = 0

def change_tmp_table(tmp_table, sr, sc, ar, ac):
    if table[sr][sc] == table[ar][ac]:
        return
    diff = (table[sr][sc] - table[ar][ac]) // 4
    tmp_table[sr][sc] -= diff
    tmp_table[ar][ac] += diff


def balance():
    tmp_table = [[0] * (m + 1) for _ in range(n + 1)]
    for r in range(1, n):
        for c in range(1, m+1):
            if blocks[r][c][3]:
                continue
            if table[r][c] > table[r+1][c]:
                change_tmp_table(tmp_table, r, c, r+1, c)
            else:
                change_tmp_table(tmp_table, r+1, c, r, c)

    for r in range(1, n+1):
        for c in range(1, m):
            if blocks[r][c][0]:
                continue
            if table[r][c] > table[r][c+1]:
                change_tmp_table(tmp_table, r, c, r, c+1)
            else:
                change_tmp_table(tmp_table, r, c+1, r, c)

    for r in range(1, n+1):
        for c in range(1, m+1):
            table[r][c] += tmp_table[r][c]


def minus(r, c):
    if table[r][c]:
        table[r][c] -= 1


def minus_edges():
    for c in range(1, m+1):
        minus(1, c)
        minus(n, c)
    for r in range(2, n):
        minus(r, 1)
        minus(r, m)


def check_all():
    for r, c in check_list:
        if table[r][c] < k:
            return False
    return True


while True:
    # 1. 바람 나옴
    wind()
    # 2. 온도가 조절됨
    balance()

    # 3. 가장 바깥쪽 온도 줄어듦
    minus_edges()
    # 4. 초콜릿 먹음
    chocolate += 1
    # 5. 모든 칸의 온도가 k 이상인지 검사
    if check_all() or chocolate == 101:
        break


print(chocolate)





