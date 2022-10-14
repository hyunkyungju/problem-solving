import copy

def init():
    init_n, _ = map(int, input().split())
    init_table = []
    for _ in range(init_n):
        init_table.append(list(map(int, input().split())))
    return init_n, init_table


def in_range(nr, nc):
    return 0 <= nr < n and 0 <= nc < n


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(vr, vc, is_visited, color):
    if is_visited[vr][vc]:
        return []
    is_visited[vr][vc] = True
    route = [(vr, vc)]
    for i in range(4):
        nr = vr + dr[i]
        nc = vc + dc[i]
        if in_range(nr, nc) and not is_visited[nr][nc] and (table[nr][nc] == color or not table[nr][nc]):
            route += dfs(nr, nc, is_visited, color)

    return route

def get_rainbows(route):
    rainbows = []
    for r, c in route:
        if table[r][c] == 0:
            rainbows.append((r, c))
    return rainbows


def find_blocks():
    is_visited = [[False] * n for _ in range(n)]
    max_route = [0]
    max_rainbow_cnt = n ** 2
    for r in range(n):
        for c in range(n):
            if not is_visited[r][c] and table[r][c] >= 1:
                route = dfs(r, c, is_visited, table[r][c])
                rainbows = get_rainbows(route)
                rainbow_cnt = len(rainbows)
                for rainbow_r, rainbow_c in rainbows:
                    is_visited[rainbow_r][rainbow_c] = False
                if len(route) > len(max_route) or (len(route) == len(max_route) and rainbow_cnt >= max_rainbow_cnt):
                    max_route = route
                    max_rainbow_cnt = rainbow_cnt

    return max_route


def remove_block_group(block_group):
    for r, c in block_group:
        table[r][c] = -2


def gravity():
    for c in range(n):
        empty = 0
        for r in range(n - 1, -1, -1):
            if table[r][c] == -2:
                empty += 1
            elif table[r][c] == -1:
                empty = 0
            else:
                table[r + empty][c], table[r][c] = table[r][c], table[r + empty][c]


def rotate():
    global table
    tmp_table = [[-2] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            tmp_table[n - c - 1][r] = table[r][c]
    table = copy.deepcopy(tmp_table)




def sol():
    score = 0
    while True:
        # 1. 블록 그룹 찾기
        block_group = find_blocks()
        if len(block_group) < 2:
            break

        # 2. 블록그룹 제거
        remove_block_group(block_group)
        score += len(block_group) ** 2
        # 3. 중력
        gravity()

        # 4. 회전
        rotate()
        # 5. 중력
        gravity()
    print(score)


t = 1
for it in range(t):
    n, table = init()
    sol()
