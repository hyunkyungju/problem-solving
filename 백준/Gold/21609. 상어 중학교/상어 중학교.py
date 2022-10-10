def print_table():
    for r in range(1, n+1):
        for c in range(1, n+1):
            if c > 1 and table[r][c-1] > 0:
                print(' ', end='')
            print(table[r][c], end=' ')
        print()
    print("=======================")

n, m = map(int, input().split())
table = [[-2]*(n+1)]
for _ in range(n):
    lst = [-2]
    lst.extend(list(map(int, input().split())))
    table.append(lst)


def in_range(nr, nc):
    return 1 <= nr < n+1 and 1 <= nc < n+1


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(vr, vc, rcolor, is_find_blocks = False):
    if visited[vr][vc] or rainbow_visited[vr][vc]:
        return 0, 0
    if is_find_blocks:
        route.append((vr, vc))
    cnt = 1
    rainbow_cnt = 0
    vcolor = table[vr][vc]
    if vcolor == 0:
        rainbow_cnt = 1
        rainbow_visited[vr][vc] = True
    else:
        visited[vr][vc] = True
    for idx in range(4):
        nr = vr + dr[idx]
        nc = vc + dc[idx]
        if not in_range(nr, nc):
            continue
        if (not visited[nr][nc] and table[nr][nc] == rcolor) or (not rainbow_visited[nr][nc] and table[nr][nc] == 0):
            tmp_cnt, tmp_rainbow_cnt = dfs(nr, nc, rcolor, is_find_blocks)
            cnt += tmp_cnt
            rainbow_cnt += tmp_rainbow_cnt
    return cnt, rainbow_cnt


def remove_blocks():
    for vr, vc in route:
        table[vr][vc] = -2




def gravity():
    for c in range(1, n+1):
        empty_cnt = 0
        is_empty_continued = True
        r = n
        while r > 0:
            if table[r][c] == -2:
                if is_empty_continued:
                    empty_cnt += 1
                else:
                    empty_cnt = 1
                    is_empty_continued = True
            elif table[r][c] == -1:
                is_empty_continued = False
                empty_cnt = 0
            elif table[r][c] >= 0:
                if empty_cnt > 0:
                    table[r+empty_cnt][c] = table[r][c]
                    table[r][c] = -2
                else:
                    is_empty_continued = False

            r -= 1



def rotate():
    global table
    tmp_table = [[-2] * (n+1) for _ in range(n+1)]
    for r in range(1, n+1):
        for c in range(1, n+1):
            tmp_table[n-c+1][r] = table[r][c]
    table = tmp_table


score = 0
while True:
    visited = [[False]*(n+1) for _ in range(n+1)]
    max_count = 1
    max_rainbow = 0
    max_r = 0
    max_c = 0
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            color = table[r][c]
            if color > 0 and not visited[r][c]:
                if r==4:
                    pass
                rainbow_visited = [[False] * (n + 1) for _ in range(n + 1)]
                count, rainbow_count = dfs(r, c, color)
                if count < 2:
                    continue
                if count > max_count or (count == max_count and rainbow_count >= max_rainbow):
                    max_count = count
                    max_rainbow = rainbow_count
                    max_r = r
                    max_c = c

    if max_count == 1:
        break
    score += (max_count**2)
    # 길찾기
    rainbow_visited = [[False] * (n + 1) for _ in range(n + 1)]
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    route = []
    dfs(max_r, max_c, table[max_r][max_c], True)
    remove_blocks()
    gravity()
    rotate()
    gravity()

print(score)


