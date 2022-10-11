

n, m = map(int, input().split())
table = [[]]
for _ in range(n):
    lst = [-1]
    lst.extend(list(map(int, input().split())))
    table.append(lst)

moves = []
for _ in range(m):
    di, si = map(int, input().split())
    moves.append((di, si))

dr = [None, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [None, -1, -1, 0, 1, 1, 1, 0, -1]

di_dr = [-1, -1, 1, 1]
di_dc = [-1, 1, -1, 1]


def get_idx(nr, nc):
    tmp_nr = (nr-1) % n + 1
    tmp_nc = (nc-1) % n + 1
    return tmp_nr, tmp_nc


def in_table(nr, nc):
    return 1 <= nr < n+1 and 1 <= nc < n+1


clouds = [[False]*(n+1) for _ in range(n+1)]
clouds[n-1][1] = True
clouds[n-1][2] = True
clouds[n][1] = True
clouds[n][2] = True

def print_t(t):
    for r in range(1, n+1):
        for c in range(1, n+1):
            print(t[r][c], end=' ')
        print()
    print("**************")

def move_clouds(d, s):
    global clouds
    tmp_clouds = [[False]*(n+1) for _ in range(n+1)]
    for r in range(1, n+1):
        for c in range(1, n+1):
            if clouds[r][c]:
                nr, nc = r+dr[d]*s, c+dc[d]*s
                nr, nc = get_idx(nr, nc)
                tmp_clouds[nr][nc] = True
    clouds = tmp_clouds


def rain():
    for r in range(1, n+1):
        for c in range(1, n+1):
            if clouds[r][c]:
                table[r][c] += 1


def add_rain_consider_diagonal():
    for r in range(1, n+1):
        for c in range(1, n+1):
            if not clouds[r][c]:
                continue
            for idx in range(4):
                nr = r + di_dr[idx]
                nc = c + di_dc[idx]
                if in_table(nr, nc) and table[nr][nc] > 0:
                    table[r][c] += 1


def make_clouds():
    global clouds
    tmp_clouds = [[False]*(n+1) for _ in range(n+1)]
    for r in range(1, n+1):
        for c in range(1, n+1):
            if not clouds[r][c] and table[r][c] >= 2:
                tmp_clouds[r][c] = True
                table[r][c] -= 2
    clouds = tmp_clouds


for mi in range(m):
    di, si = moves[mi]
    # 1. 구름 이동
    move_clouds(di, si)

    # 2. 비내림
    rain()

    # 3. 구름 사라짐

    # 4. 대각선 고려해서 물 증가
    add_rain_consider_diagonal()

    # 5. 구름 생김
    make_clouds()

ans = 0
for r in range(1, n+1):
    for c in range(1, n+1):
        ans += table[r][c]
print(ans)