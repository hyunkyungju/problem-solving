
t = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def in_range(nr, nc):
    return 0 <= nr < n and 0 <= nc < n


def dfs(sr, sc, h, is_cut, l):
    global max_l
    if is_visited[sr][sc]:
        return
    is_visited[sr][sc] = True
    max_l = max(max_l, l)

    for i in range(4):
        nr = sr + dr[i]
        nc = sc + dc[i]
        if not in_range(nr, nc) or is_visited[nr][nc]:
            continue
        nh = table[nr][nc]
        if h > nh:
            dfs(nr, nc, nh, is_cut, l+1)
        elif not is_cut:
            diff = nh - h
            if diff + 1 > k:
                continue
            dfs(nr, nc, nh-(diff+1), True, l+1)
    is_visited[sr][sc] = False




for i in range(t):
    n, k = map(int, input().split())
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))

    max_l = 0
    maxes = [max(lst) for lst in table]
    max_h = max(maxes)
    is_visited = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if table[r][c] == max_h:
                dfs(r, c, max_h, False, 1)
    print(f"#{i+1} {max_l}")