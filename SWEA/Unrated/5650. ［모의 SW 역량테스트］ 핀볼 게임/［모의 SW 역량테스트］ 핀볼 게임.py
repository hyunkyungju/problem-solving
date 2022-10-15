

t = int(input())


def init():
    n = int(input())
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))
    warm_holls = [[] for _ in range(5)]
    for r in range(n):
        for c in range(n):
            val = table[r][c]
            if 6 <= val <= 10:
                warm_holls[val-6].append((r, c))

    return n, table, warm_holls


def in_range(nr, nc):
    return 0 <= nr < n and 0 <= nc < n


def get_direction(tri_d, r, c, d):
    rd = False
    if tri_d == 1:
        if d == 2:
            rd = True
        elif d == 1:
            rd = True
    elif tri_d == 2:
        if d == 0:
            rd = True
        elif d == 1:
            rd = True
    elif tri_d == 3:
        if d == 0:
            rd = True
        elif d == 3:
            rd = True
    elif tri_d == 4:
        if d == 3:
            rd = True
        elif d == 2:
            rd = True
    if not rd:
        return r, c, (d+2)%4
    else:
        return r+dr[d], c+dc[d], d


def get_pair(r, c, val):
    pair_candys = warms[val-6]
    for (hr, hc) in pair_candys:
        if not (hr==r and hc==c):
            return hr, hc



def get_tri_init(r, c, d):
    tri_d = table[r][c]
    rd = -1
    if tri_d == 1:
        if d == 2:
            rd = 3
        elif d == 1:
            rd = 0
    elif tri_d == 2:
        if d == 0:
            rd = 3
        elif d == 1:
            rd = 2
    elif tri_d == 3:
        if d == 0:
            rd = 1
        elif d == 3:
            rd = 2
    elif tri_d == 4:
        if d == 3:
            rd = 0
        elif d == 2:
            rd = 1
    return rd


dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def sol_one(sr, sc, sd):
    #print("sr", sr, "sc", sc, "sd", sd)
    score = 0
    br, bc, bd = sr, sc, sd
    while True:
        #print(br, bc, bd)
        rd = get_tri_init(br, bc, bd)
        if rd != -1:
            bd = rd
            score += 1
        b_val = table[br][bc]
        nr = br + dr[bd]
        nc = bc + dc[bd]
        before_br = br
        before_bc = bc
        if not in_range(nr, nc):
            score += 1
            bd = (bd + 2) % 4
        else:
            val = table[nr][nc]
            if not val:
                br, bc = nr, nc
            elif 1 <= val <= 5:
                score += 1
                before_d = bd
                br, bc, bd = get_direction(val, br, bc, bd)
                if before_d == bd:
                    score -= 1
            elif 6 <= val <= 10:
                br, bc = get_pair(nr, nc, val)
            elif val == -1:
                return score
        if before_br == br and before_bc == bc and 6 <= b_val <= 10:
            br, bc = get_pair(br, bc, b_val)
        if br == sr and bc == sc:
            return score



def sol():
    ans = 0
    for r in range(n):
        for c in range(n):
            if not table[r][c]:
                for d in range(4):
                    score = sol_one(r, c, d)
                    ans = max(ans, score)
    return ans

for i in range(t):
    n, table, warms = init()
    i_ans = sol()
    print(f"#{i+1} {i_ans}")
