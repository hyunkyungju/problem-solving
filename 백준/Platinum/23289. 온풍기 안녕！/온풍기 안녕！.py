from collections import deque

def print_table(table):
    for i in range(1, r+1):
        for j in range(1, c+1):
            print(table[i][j], end=' ')
        print()
    print("----")


def change(tmp_table, q, is_visited, nr, nc, power):
    tmp_table[nr][nc] += power - 1
    is_visited[nr][nc] = True
    if power > 1:
        q.append((nr, nc, power - 1))


def in_range(vr, vc):
    return 0 < vr < r+1 and 0 < vc < c+1


def bfs_initialize(sr, sc, tmp_table):
    is_visited = [[False]*(c+1) for _ in range(r + 1)]
    q = deque()
    q.append((sr, sc, 5))
    is_visited[sr][sc] = True
    tmp_table[sr][sc] += 5
    return is_visited, q


def left_bfs(sr, sc, tmp_table):
    is_visited, q = bfs_initialize(sr, sc, tmp_table)
    while q:
        vr, vc, power = q.popleft()
        nr, nc = vr - 1, vc - 1
        if in_range(nr, nc) and not wall[vr][vc][0] and not wall[vr-1][vc-1][1] and not is_visited[nr][nc]:
            change(tmp_table, q, is_visited, nr, nc, power)
        nr += 1
        if in_range(nr, nc) and not wall[vr][vc-1][1] and not is_visited[nr][nc]:
            change(tmp_table, q, is_visited, nr, nc, power)
        nr += 1
        if in_range(nr, nc) and not wall[vr+1][vc][0] and not wall[vr+1][vc-1][1] and not is_visited[nr][nc]:
            change(tmp_table, q, is_visited, nr, nc, power)



def right_bfs(sr, sc, tmp_table):
    is_visited, q = bfs_initialize(sr, sc, tmp_table)
    while q:
        vr, vc, power = q.popleft()
        nr, nc = vr - 1, vc + 1
        if in_range(nr, nc) and not wall[vr][vc][0] and not wall[vr-1][vc][1] and not is_visited[nr][nc]:
            change(tmp_table, q, is_visited, nr, nc, power)
        nr += 1
        if in_range(nr, nc) and not wall[vr][vc][1] and not is_visited[nr][nc]:
            change(tmp_table, q, is_visited, nr, nc, power)
        nr += 1
        if in_range(nr, nc) and not wall[vr+1][vc][0] and not wall[vr+1][vc][1] and not is_visited[nr][nc]:
            change(tmp_table, q, is_visited, nr, nc, power)


def up_bfs(sr, sc, tmp_table):
    is_visited, q = bfs_initialize(sr, sc, tmp_table)
    while q:
        vr, vc, power = q.popleft()
        nr, nc = vr-1 , vc-1
        if in_range(nr, nc) and not wall[vr][vc-1][1] and not wall[vr][vc-1][0] and not is_visited[nr][nc]:
            change(tmp_table, q, is_visited, nr, nc, power)
        nc += 1
        if in_range(nr, nc) and not wall[vr][vc][0] and not is_visited[nr][nc]:
            change(tmp_table, q, is_visited, nr, nc, power)
        nc += 1
        if in_range(nr, nc) and not wall[vr][vc][1] and not wall[vr][vc+1][0] and not is_visited[nr][nc]:
            change(tmp_table, q, is_visited, nr, nc, power)



def down_bfs(sr, sc, tmp_table):
    is_visited, q = bfs_initialize(sr, sc, tmp_table)
    while q:
        vr, vc, power = q.popleft()
        nr, nc = vr+1 , vc-1
        if in_range(nr, nc) and not wall[vr][vc-1][1] and not wall[vr+1][vc-1][0] and not is_visited[nr][nc]:
            change(tmp_table, q, is_visited, nr, nc, power)
        nc += 1
        if in_range(nr, nc) and not wall[vr+1][vc][0] and not is_visited[nr][nc]:
            change(tmp_table, q, is_visited, nr, nc, power)
        nc += 1
        if in_range(nr, nc) and not wall[vr][vc][1] and not wall[vr+1][vc+1][0] and not is_visited[nr][nc]:
            change(tmp_table, q, is_visited, nr, nc, power)




def machine():
    tmp_table = [[0]*(c+1) for _ in range(r+1)]
    for mr, mc, md in machines:
        if md == 1:
            tr, tc = mr, mc+1
            right_bfs(tr, tc, tmp_table)
        elif md == 2:
            tr, tc = mr, mc-1
            left_bfs(tr, tc, tmp_table)
        elif md == 3:
            tr, tc = mr-1, mc
            up_bfs(tr, tc, tmp_table)
        elif md == 4:
            tr, tc = mr+1, mc
            down_bfs(tr, tc, tmp_table)
    for i in range(1, r+1):
        for j in range(1, c+1):
            table[i][j] += tmp_table[i][j]


def control_diff(tmp_table, bigi, smalli, bigj, smallj):
    if table[bigi][bigj] == table[smalli][smallj]:
        return
    diff = (table[bigi][bigj] - table[smalli][smallj]) // 4
    tmp_table[bigi][bigj] -= diff
    tmp_table[smalli][smallj] += diff


def control():
    tmp_table = [[0]*(c+1) for _ in range(r+1)]
    for i in range(1, r+1):
        for j in range(1, c):
            if not wall[i][j][1]:
                if table[i][j] >= table[i][j+1]+4:
                    diff = (table[i][j] - table[i][j+1]) // 4
                    tmp_table[i][j] -= diff
                    tmp_table[i][j+1] += diff
                elif table[i][j]+4 <= table[i][j+1]:
                    diff = (table[i][j+1] - table[i][j]) // 4
                    tmp_table[i][j+1] -= diff
                    tmp_table[i][j] += diff

                # bigi, smalli, bigj, smallj = i, i, j, j+1
                # if table[i][j] < table[i][j+1]:
                #     bigj = j+1
                #     smallj = j
                # control_diff(tmp_table, bigi, smalli, bigj, smallj)

    for i in range(1, r):
        for j in range(1, c+1):
            if not wall[i+1][j][0]:
                if table[i][j] >= table[i+1][j]+4:
                    diff = (table[i][j] - table[i+1][j]) // 4
                    tmp_table[i][j] -= diff
                    tmp_table[i+1][j] += diff
                elif table[i][j]+4 <= table[i+1][j]:
                    diff = (table[i+1][j] - table[i][j]) // 4
                    tmp_table[i+1][j] -= diff
                    tmp_table[i][j] += diff

                # bigi, smalli, bigj, smallj = i, i+1, j, j
                # if table[i][j] < table[i+1][j]:
                #     bigi = i+1
                #     smalli = i
                # control_diff(tmp_table, bigi, smalli, bigj, smallj)
    for i in range(1, r+1):
        for j in range(1, c+1):
            table[i][j] += tmp_table[i][j]


def cold_outside():
    for i in range(1, r+1):
        table[i][1] = max(0, table[i][1]-1)
        table[i][c] = max(0, table[i][c]-1)
    for j in range(2, c):
        table[1][j] = max(0, table[1][j]-1)
        table[r][j] = max(0, table[r][j]-1)


def check():
    for cr, cc in checks:
        if table[cr][cc] < k:
            return False
    return True


r, c, k = map(int, input().split())
machines = []
checks = []

for i in range(1, r+1):
    lst = [0]
    lst.extend(list(map(int, input().split())))
    for j in range(1, c+1):
        value = lst[j]
        if value == 5:
            checks.append((i, j))
        elif value == 0:
            pass
        else:
            machines.append((i, j, value))
table = [[0]*(c+1) for _ in range(r+1)]
w = int(input())
wall = [[[False, False] for _ in range(c+1)] for _ in range(r+1)]

for _ in range(w):
    x, y, t = map(int, input().split())
    wall[x][y][t] = True



for i in range(100):
    machine()
    control()
    cold_outside()
    if check():
       print(i+1)
       exit()


print(101)

