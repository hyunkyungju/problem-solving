direction = ['e', 's', 'w', 'n']
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m, k = map(int, input().split())
table = [[]]
for _ in range(n):
    lst = [0]
    lst.extend(list(map(int, input().split())))
    table.append(lst)

figure = [2, 1, 5, 6, 4, 3]
d = 'e'
r, c = 1, 1
score = 0


def change_north():
    global figure
    f = [0] * 6
    f[0] = figure[1]
    f[1] = figure[2]
    f[2] = figure[3]
    f[3] = figure[0]
    f[4] = figure[4]
    f[5] = figure[5]
    figure = f


def change_south():
    global figure
    f = [0] * 6
    f[0] = figure[3]
    f[1] = figure[0]
    f[2] = figure[1]
    f[3] = figure[2]
    f[4] = figure[4]
    f[5] = figure[5]
    figure = f


def change_west():
    global figure
    f = [0] * 6
    f[0] = figure[0]
    f[1] = figure[5]
    f[2] = figure[2]
    f[3] = figure[4]
    f[4] = figure[1]
    f[5] = figure[3]
    figure = f


def change_east():
    global figure
    f = [0] * 6
    f[0] = figure[0]
    f[1] = figure[4]
    f[2] = figure[2]
    f[3] = figure[5]
    f[4] = figure[3]
    f[5] = figure[1]
    figure = f


def change_figure():
    if d == 'n':
        change_north()
    elif d == 's':
        change_south()
    elif d == 'w':
        change_west()
    elif d == 'e':
        change_east()
    else:
        print("error in change figure")


def get_idx_nr():
    idx = direction.index(d)
    nr = r + dr[idx]
    return idx, nr


def get_idx_nc():
    idx = direction.index(d)
    nc = c + dc[idx]
    return idx, nc


def roll():
    global d, r, c
    idx, nr = get_idx_nr()
    if nr > n:
        d = 'n'
        idx, nr = get_idx_nr()
    elif nr < 1:
        d = 's'
        idx, nr = get_idx_nr()

    idx, nc = get_idx_nc()
    if nc > m:
        d = 'w'
        idx, nc = get_idx_nc()
    elif nc < 1:
        d = 'e'
        idx, nc = get_idx_nc()
    r, c = nr, nc
    change_figure()




def change_direction():
    global d
    a = figure[3]
    b = table[r][c]
    idx = direction.index(d)
    if a > b: # 시계 방향
        idx = (idx+1) % 4
    elif a < b:
        idx = (idx-1) % 4
    else:
        return
    d = direction[idx]

cnt = 0

def dfs(visited, r, c, b):
    global cnt
    cnt += 1
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if nr > n or nr < 1 or nc > m or nc < 1:
            continue
        if not visited[nr][nc] and table[nr][nc] == b:
            visited[nr][nc] = True
            dfs(visited, nr, nc, b)



for _ in range(k):
    cnt = 0
    roll()
    visited = [[False] * (m+1) for _ in range(n+1)]
    visited[r][c] = True
    b = table[r][c]
    dfs(visited, r, c, b)
    score += b * cnt
    change_direction()


print(score)