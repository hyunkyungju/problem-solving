def table_number_initialize():
    drs = [0, 1, 0, -1]
    dcs = [-1, 0, 1, 0]
    num_lst = [[] for _ in range(n**2)]
    r, c = (n+1)//2, (n+1)//2
    cnt = 1
    di = 0
    num = 1
    while num < n**2:
        dr, dc = drs[di], dcs[di]
        for _ in range(int(cnt)):
            r += dr
            c += dc
            num_lst[num] = (r, c)
            num += 1
            if num == n**2:
                break
        cnt += 0.5
        di = (di+1)%4
    return num_lst


n, m = map(int, input().split())
table = [[]]
magics = []
for _ in range(n):
    lst = [0]
    lst.extend(list(map(int, input().split())))
    table.append(lst)

for _ in range(m):
    di, si = map(int, input().split())
    magics.append((di, si))

bombs = [None, 0, 0, 0]

number_lst = table_number_initialize()


dr = [None, -1, 1, 0, 0]
dc = [None, 0, 0, -1, 1]

def in_range(nr, nc):
    return 1 <= nr < n+1 and 1 <= nc < n+1

def break_balls(d, s):
    r, c = (n+1)//2, (n+1)//2
    for i in range(s):
        r += dr[d]
        c += dc[d]
        table[r][c] = 0




def move_balls():
    amount = 1
    for i in range(2, n**2):
        r, c = number_lst[i]
        br, bc = number_lst[i-amount]
        if table[br][bc] == 0:
            if table[r][c] == 0:
                amount += 1
            else:
                table[br][bc] = table[r][c]
                table[r][c] = 0


def bomb_action(last_num, continued_amount, score):
    bombs[score] += continued_amount
    for num in range(last_num, last_num-continued_amount, -1):
        r, c = number_lst[num]
        table[r][c] = 0




def bomb_balls():
    continued_val = 0
    continued_amount = 1
    for num in range(1, n**2):
        r, c = number_lst[num]
        val = table[r][c]
        if val == 0:
            # 마지막
            if continued_amount >= 4:
                bomb_action(num-1, continued_amount, continued_val)
            break
        if val == continued_val:
            continued_amount += 1
        else:
            if continued_amount >= 4:
                bomb_action(num-1, continued_amount, continued_val)
            continued_val = val
            continued_amount = 1




def change_balls():
    global table
    tmp_table = [[0]*(n+1) for _ in range(n+1)]
    continued_val = 0
    continued_amount = 1
    new_num = 1
    for num in range(1, n ** 2):
        r, c = number_lst[num]
        val = table[r][c]
        if val == 0:
            break
        if val == continued_val:
            continued_amount += 1
        else:
            if continued_val:
                a, b = continued_amount, continued_val
                nr1, nc1 = number_lst[new_num]
                nr2, nc2 = number_lst[new_num+1]
                tmp_table[nr1][nc1] = a
                tmp_table[nr2][nc2] = b
                new_num += 2
            continued_val = val
            continued_amount = 1
        if new_num >= n**2:
            break

    if new_num < n**2 and continued_val > 0:
        a, b = continued_amount, continued_val
        nr1, nc1 = number_lst[new_num]
        nr2, nc2 = number_lst[new_num + 1]
        tmp_table[nr1][nc1] = a
        tmp_table[nr2][nc2] = b
    table = tmp_table



for mi in range(m):
    # 1. 구슬 파괴
    di, si = magics[mi]
    break_balls(di, si)
    # 2. 구슬 이동
    move_balls()
    while True:
        # 3. 구슬 폭발
        b_sum_bomb = sum(bombs[1:])
        bomb_balls()
        a_sum_bomb = sum(bombs[1:])
        # 4. 구슬 이동
        move_balls()
        if b_sum_bomb == a_sum_bomb:
            break
    # 5. 구슬 변화
    change_balls()
ans = 0
for i in range(1, 4):
    ans += bombs[i] * i
print(ans)



# 1h 30m 사용!