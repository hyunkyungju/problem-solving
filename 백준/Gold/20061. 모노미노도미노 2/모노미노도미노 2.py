
n = int(input())
blocks = []
for _ in range(n):
    t, x, y = map(int, input().split())
    blocks.append((t, x, y))

greens = [[0]*4 for _ in range(6)]
blues = [[0]*4 for _ in range(6)]


def put_one(col, table):
    row = 5
    for r in range(6):
        if table[r][col]:
            row = r-1
            break
    table[row][col] = 1
    return row, col


def put_two_vertical(col, table):
    r, c = put_one(col, table)
    table[r-1][col] = 1


def put_two_horizontal(col, table):
    row = 5
    for r in range(6):
        if table[r][col] or table[r][col+1]:
            row = r-1
            break
    table[row][col] = 1
    table[row][col + 1] = 1
    return row, col


def put_block_green(bt, br, bc):
    if bt == 1:
        col = bc
        put_one(col, greens)
    elif bt == 3:
        col = bc
        put_two_vertical(col, greens)
    elif bt == 2:
        col = bc
        put_two_horizontal(col, greens)


def put_block_blue(bt, br, bc):
    if bt == 1:
        col = 3-br
        put_one(col, blues)
    elif bt == 2:
        col = 3-br
        put_two_vertical(col, blues)
    elif bt == 3:
        col = 2-br
        put_two_horizontal(col, blues)



def put_block(bt, br, bc):
    put_block_green(bt, br, bc)
    put_block_blue(bt, br, bc)


def tetris_impl(table):
    global score
    cnt = 0
    for r in range(5, -1, -1):
        if sum(table[r]) == 4:
            score += 1
            cnt += 1
        else:
            table[r+cnt] = table[r]
        if cnt:
            table[r] = [0, 0, 0, 0]


def tetris():
    tetris_impl(greens)
    tetris_impl(blues)



def check_blur_impl(table):
    blur_num = 0
    for r in range(2):
        if sum(table[r]):
            blur_num += 1
    if not blur_num:
        return
    for r in range(5, 5-blur_num, -1):
        table[r] = [0, 0, 0, 0]
    for r in range(5-blur_num, -1, -1):
        table[r+blur_num] = table[r]
        table[r] = [0, 0, 0, 0]



def check_blur():
    check_blur_impl(greens)
    check_blur_impl(blues)


def board_num_impl(table):
    cnt = 0
    for r in range(6):
        for c in range(4):
            if table[r][c]:
                cnt += 1
    return cnt

def get_board_num():
    green_cnt = board_num_impl(greens)
    blue_cnt = board_num_impl(blues)
    return green_cnt + blue_cnt


score = 0

for block in blocks:
    t, x, y = block
    put_block(t, x, y)

    tetris()
    check_blur()


print(score)
board_num = get_board_num()
print(board_num)

# 1h 4m 소요