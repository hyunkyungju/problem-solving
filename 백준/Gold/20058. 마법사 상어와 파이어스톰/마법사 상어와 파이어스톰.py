n, q = map(int, input().split())
table = [[]]
for _ in range(2**n):
    lst = [0]
    lst.extend(list(map(int, input().split())))
    table.append(lst)
levels = list(map(int, input().split()))


def rotate_impl(sr, sc, tile_size):
    tmp = [[-1] * (tile_size+1) for _ in range(tile_size+1)]
    for r in range(1, tile_size+1):
        for c in range(1, tile_size+1):
            tmp[c][tile_size-r+1] = table[sr+r][sc+c]

    for r in range(1, tile_size+1):
        for c in range(1, tile_size+1):
            table[sr + r][sc + c] = tmp[r][c]



def rotate(l):
    tile_size = 2**l
    tile_num = int(2**n // tile_size)
    for i in range(tile_num):
        for j in range(tile_num):
            r = i * tile_size
            c = j * tile_size
            rotate_impl(r, c, tile_size)


def in_range(nr, nc):
    return 1 <= nr < 2**n+1 and 1 <= nc < 2**n+1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def ice_minus():
    minus_idxes = []
    for r in range(1, 2**n+1):
        for c in range(1, 2**n+1):
            if table[r][c] == 0:
                continue
            iced_neighbor = 0
            for idx in range(4):
                nr = r + dr[idx]
                nc = c + dc[idx]
                if in_range(nr, nc) and table[nr][nc] > 0:
                    iced_neighbor += 1
            if iced_neighbor < 3:
                minus_idxes.append((r, c))
    for r, c in minus_idxes:
        table[r][c] -= 1


def count_ice():
    cnt = 0
    for r in range(1, 2**n+1):
        for c in range(1, 2**n+1):
            cnt += table[r][c]
    return cnt


def dfs(start_r, start_c):
    cnt = 0
    s = []
    s.append((start_r, start_c))
    while s:
        sr, sc = s.pop()
        if is_visited[sr][sc]:
            continue
        cnt += 1
        is_visited[sr][sc] = True
        for i in range(4):
            nr = sr + dr[i]
            nc = sc + dc[i]
            if in_range(nr, nc) and not is_visited[nr][nc] and table[nr][nc] > 0:
                s.append((nr, nc))

    return cnt


def print_table():
    for r in range(1, 2**n+1):
        for c in range(1, 2**n+1):
            print(table[r][c], end = ' ')
        print()
    print("==============")

def get_max_icebox():
    max_cnt = 0
    for r in range(1, 2**n+1):
        for c in range(1, 2**n+1):
            if not is_visited[r][c] and table[r][c] > 0:
                cnt = dfs(r, c)
                max_cnt = max(max_cnt, cnt)
    return max_cnt


for i in range(q):
    rotate(levels[i])
    ice_minus()

# n = 6
# table = [[1]*65 for _ in range(65)]
ice_num = count_ice()
is_visited = [[False]*(2**n+1) for _ in range(2**n+1)]
max_icebox = get_max_icebox()
print(ice_num)
print(max_icebox)

'''
3 1
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32
33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48 
49 50 51 52 53 54 55 56
57 58 59 60 61 62 63 64
1


'''
# 1h 35m
# dfs는 재귀 한도가 1000이다.