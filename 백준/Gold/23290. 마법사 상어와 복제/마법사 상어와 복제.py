

def print_table(table):
    for i in range(1, 5):
        for j in range(1, 5):
            print(table[i][j], end='')
        print()
    print("-----------------------")


def copy_magic():
    for i in range(1, 5):
        for j in range(1, 5):
            if fish_table[i][j]:
                copy_table[i][j] = fish_table[i][j].copy()


def can_go(dr, dc):
    if not (0<dr<5 and 0<dc<5):
        return False
    if dr == sr and dc == sc:
        return False
    if smell_table[dr][dc] != -1:
        return False
    return True


def move_fish():
    global fish_table
    tmp_table = [[[] for _ in range(5)] for _ in range(5)]
    for r in range(1, 5):
        for c in range(1, 5):
            for fish_d in fish_table[r][c]:
                is_found = False
                for idx in range(8):
                    di = (fish_d-idx-1)%8 + 1
                    nr = r + dr[di]
                    nc = c + dc[di]
                    if can_go(nr, nc):
                        tmp_table[nr][nc].append(di)
                        is_found = True
                        break
                if not is_found:
                    tmp_table[r][c].append(fish_d)
    fish_table = [[[] for _ in range(5)] for _ in range(5)]
    for r in range(1, 5):
        for c in range(1, 5):
            fish_table[r][c] = tmp_table[r][c]


dsr = [None, -1, 0, 1, 0]
dsc = [None, 0, -1, 0, 1]


def in_range(r, c):
    return 0<r<5 and 0<c<5


max_route = []
max_removed_fish = -1
max_sr = 0
max_sc = 0

def get_removed_fish(route):
    route = list(set(route))
    cnt = 0
    for r, c in route:
        cnt += len(fish_table[r][c])
    return cnt


def move_shark_dfs(r, c, route):
    global max_removed_fish
    global max_route
    global max_sr, max_sc
    if len(route) == 3:
        removed_fish = get_removed_fish(route)
        if removed_fish > max_removed_fish:
            max_removed_fish = removed_fish
            max_route = route[:]
            max_sr, max_sc = route[-1]
        return
    for idx in range(1, 5):
        nr = r+dsr[idx]
        nc = c+dsc[idx]
        if in_range(nr, nc):
            ro = route[:]
            ro.append((nr, nc))
            move_shark_dfs(nr, nc, ro)


def move_shark():
    global max_route, max_removed_fish, sr, sc, max_sr, max_sc
    max_route = []
    max_removed_fish = -1
    max_sr, max_sc = sr, sc
    move_shark_dfs(sr, sc, [])
    for r, c in max_route:
        if fish_table[r][c]:
            smell_table[r][c] = 0
            fish_table[r][c] = []
    sr, sc = max_sr, max_sc


def remove_smell():
    for r in range(1, 5):
        for c in range(1, 5):
            smell_day = smell_table[r][c]
            if smell_day == 2:
                smell_table[r][c] = -1
            elif smell_day > -1:
                smell_table[r][c] += 1


def copy_fish():
    for r in range(1, 5):
        for c in range(1, 5):
            fish_table[r][c].extend(copy_table[r][c])


m, s = map(int, input().split())
fish_table = [[[] for _ in range(5)] for _ in range(5)]
for _ in range(m):
    fx, fy, d = map(int, input().split())
    fish_table[fx][fy].append(d)
sr, sc = map(int, input().split())
# 물고기 냄새, 복제마법이 적용됐는지 반영하는 테이블.
smell_table = [[-1]*5 for _ in range(5)]
dr = [None, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [None, -1, -1, 0, 1, 1, 1, 0, -1]


for si in range(s):
    copy_table = [[[] for _ in range(5)] for _ in range(5)]
    copy_magic()
    move_fish()
    move_shark()
    remove_smell()
    copy_fish()

ans = 0
for r in range(1, 5):
    for c in range(1, 5):
        ans += len(fish_table[r][c])
print(ans)
# 둘 이상의 물고기가 같은 칸에 있을 수도 있으며, 마법사 상어와 물고기가 같은 칸에 있을 수도 있다.
# 모든 물고기가 한 칸 이동한다. 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
