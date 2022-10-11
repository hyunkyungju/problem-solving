

def in_range(nr, nc):
    return 1 <= nr < n+1 and 1 <= nc < n+1


winds = {(0, -3): 5, (-1, -2): 10,  (1, -2): 10, (-2, -1): 2, (-1, -1): 7, (1, -1): 7, (2, -1): 2,
         (-1, 0): 1, (1, 0): 1, (0, -2): 'a'}

blow_sand = 0


def move(xr, xc, idx):
    global blow_sand
    r, c = 0, -1
    yr, yc = xr, xc
    nr_diff = [r, -c, -r, c]
    nc_diff = [c, r, -c, -r]
    yr += nr_diff[idx]
    yc += nc_diff[idx]
    y_sand = table[yr][yc]
    sand_total = 0
    for (r, c), v in winds.items():
        nr, nc = xr, xc
        nr_diff = [r, -c, -r, c]
        nc_diff = [c, r, -c, -r]
        nr += nr_diff[idx]
        nc += nc_diff[idx]
        if v == 'a':
            sand = y_sand - sand_total
        else:
            sand = int(y_sand * v / 100)
        if in_range(nr, nc):
            table[nr][nc] += sand
        else:
            blow_sand += sand
        sand_total += sand
    table[yr][yc] = 0


def track():
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    cnt = 1
    r, c = (n+1)//2, (n+1)//2
    idx = 0
    while True:
        for i in range(int(cnt)):
            if r == 1 and c == 1:
                return
            move(r, c, idx)
            r += dr[idx]
            c += dc[idx]
        cnt += 0.5
        idx = (idx+1) % 4


n = int(input())
table = [[]]
for _ in range(n):
    lst = [-1]
    lst.extend(list(map(int, input().split())))
    table.append(lst)

track()
print(blow_sand)


