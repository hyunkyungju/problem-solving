

def in_range(nr, nc):
    return 1 <= nr < n+1 and 1 <= nc < n+1


winds = {(0, -3): 5, (-1, -2): 10,  (1, -2): 10, (-2, -1): 2, (-1, -1): 7, (1, -1): 7, (2, -1): 2,
         (-1, 0): 1, (1, 0): 1}


blow_sand = 0

def move(xr, xc, idx):
    global blow_sand
    ar_diff, ac_diff = 0, -2
    yr_diff, yc_diff = 0, -1
    ar, ac, yr, yc = xr, xc, xr, xc
    if idx == 0:
        ar += ar_diff
        ac += ac_diff
        yr += yr_diff
        yc += yc_diff
    elif idx == 3:
        ar += ac_diff
        ac -= ar_diff
        yr += yc_diff
        yc -= yr_diff
    elif idx == 2:
        ar -= ar_diff
        ac -= ac_diff
        yr -= yr_diff
        yc -= yc_diff
    elif idx == 1:
        ar -= ac_diff
        ac += ar_diff
        yr -= yc_diff
        yc += yr_diff
    y_sand = table[yr][yc]
    sand_total = 0
    for (r, c), v in winds.items():
        nr, nc = xr, xc
        if idx == 0:
            nr += r
            nc += c
        elif idx == 3:
            nr += c
            nc -= r
        elif idx == 2:
            nr -= r
            nc -= c
        elif idx == 1:
            nr -= c
            nc += r
        else:
            print("eroorrr")
        sand = int(y_sand * v / 100)
        if in_range(nr, nc):
            table[nr][nc] += sand
        else:
            blow_sand += sand
        sand_total += sand
    a_sand = y_sand - sand_total
    if in_range(ar, ac):
        table[ar][ac] += a_sand
    else:
        blow_sand += a_sand

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