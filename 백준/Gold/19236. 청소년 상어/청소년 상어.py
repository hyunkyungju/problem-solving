places = [0] * 17
table = [[[-1, -1] for _ in range(4)] for _ in range(4)]
for i in range(4):
    tmps = list(map(int, input().split()))
    for j in range(4):
        a, b = tmps[2*j], tmps[2*j+1]
        places[a] = (i, j)
        table[i][j] = (a, b)

dr = [None, -1, -1, 0, 1, 1, 1, 0, -1]
dc = [None, 0, -1, -1, -1, 0, 1, 1, 1]


def eat(r, c):
    fish_num, fish_d = table[r][c]
    shark_d = fish_d
    before_shark = places[0]
    if before_shark:
        shark_r, shark_c = before_shark
        table[shark_r][shark_c] = None

    table[r][c] = (0, shark_d)

    places[fish_num] = None
    places[0] = (r, c)
    return fish_num


def in_range(nr, nc):
    return 0 <= nr < 4 and 0 <= nc < 4


def dfs(s):
    sum_s = sum(s)
    if sum_s == move_cnt:
        cases.append(s)
        return
    for i in range(1, move_cnt - sum_s + 1):
        dfs(s+[i])




def find_cases():
    global move_cnt
    sr, sc = 0, 0
    _, shark_d = table[sr][sc]
    sdr = dr[shark_d]
    sdc = dc[shark_d]
    for i in range(4):
        if in_range(sr + sdr * i, sc + sdc * i):
            move_cnt += 1
        else:
            break
    dfs([])



def move_fish():
    sr, sc = places[0]
    for num in range(1, 17):
        fish_place = places[num]
        if not fish_place:
            continue
        r, c = fish_place
        _, dir = table[r][c]
        for i in range(8):
            d = (dir+i-1)%8 +1
            nr = r+dr[d]
            nc = c+dc[d]
            if not in_range(nr, nc) or (nr==sr and nc==sc):
                continue
            if not table[nr][nc]:
                table[nr][nc] = (num, d)
                places[num] = (nr, nc)
                table[r][c] = None
            else:
                bnum, bd = table[nr][nc]
                table[nr][nc] = (num, d)
                places[num] = (nr, nc)
                table[r][c] = (bnum, bd)
                places[bnum] = (r, c)
            break


def move_shark(move_num):
    sr, sc = places[0]
    _, sd = table[sr][sc]
    nr = sr + dr[sd] * move_num
    nc = sc + dc[sd] * move_num
    if in_range(nr, nc):
        if table[nr][nc]:
            eat(nr, nc)
        else:
            return False
    return True




cases = []
move_cnt = 0
find_cases()
initial_shark_eat = eat(0, 0)
max_shark_eat = initial_shark_eat

def make_tmp():
    tmp_places = [0] * 17
    tmp_table = [[[-1, -1] for _ in range(4)] for _ in range(4)]
    for i in range(17):
        tmp_places[i] = places[i]
    for r in range(4):
        for c in range(4):
            tmp_table[r][c] = table[r][c]
    return tmp_places, tmp_table

def rollback_tmp(tmp_places, tmp_table):
    for i in range(17):
        places[i] = tmp_places[i]
    for r in range(4):
        for c in range(4):
            table[r][c] = tmp_table[r][c]

def sol(level):
    global max_shark_eat
    shark_eat = 0
    move_fish()
    sr, sc = places[0]
    _, sd = table[sr][sc]
    nr = sr
    nc = sc
    for _ in range(4):
        nr += dr[sd]
        nc += dc[sd]
        if in_range(nr, nc) and table[nr][nc]:
            tmp_places, tmp_table = make_tmp()
            this_shark_eat = eat(nr, nc)
            after_shark_eat = sol(level+1)
            shark_eat = max(shark_eat, this_shark_eat+after_shark_eat)
            rollback_tmp(tmp_places, tmp_table)

    max_shark_eat = max(max_shark_eat, shark_eat+initial_shark_eat)
    return shark_eat


sol(0)


print(max_shark_eat)