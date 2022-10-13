
n, m, k = map(int, input().split())
table = [[[0, 0, None, None] for _ in range(n+1)] for _ in range(n+1)]
prs = [None] * (m+1)


tmp_table = []
for i in range(n):
    tmp_table.append(list(map(int, input().split())))

init_shark_direction = list(map(int, input().split()))
# 0부터임

for i in range(n):
    lst = tmp_table[i]
    for j, fish in enumerate(lst):
        if fish:
            table[i+1][j+1][0] = fish
            table[i+1][j+1][3] = init_shark_direction[fish-1]



for i in range(1, m+1):
    tmp_prs = [[]]
    for _ in range(4):
        tmp_prs.append(list(map(int, input().split())))
    prs[i] = tmp_prs


def smell():
    for r in range(1, n+1):
        for c in range(1, n+1):
            if table[r][c][0]:
                table[r][c][1] = k
                table[r][c][2] = table[r][c][0]


dr = [None, -1, 1, 0, 0]
dc = [None, 0, 0, -1, 1]

def in_range(nr, nc):
    return 0 < nr < n+1 and 0 < nc < n+1

def move():
    tmp_table = [[[] for _ in range(n+1)] for _ in range(n+1)]
    for r in range(1, n+1):
        for c in range(1, n+1):
            if not table[r][c][0]:
                continue
            num = table[r][c][0]
            num_dir = table[r][c][3]
            num_prs = prs[num][num_dir]
            is_non_smell = False
            for d in num_prs:
                nr = r+dr[d]
                nc = c+dc[d]
                if in_range(nr, nc) and not table[nr][nc][1]:
                    tmp_table[nr][nc].append((num, d))
                    is_non_smell = True
                    break
            if is_non_smell:
                continue
            for d in num_prs:
                nr = r+dr[d]
                nc = c+dc[d]
                if in_range(nr, nc) and table[nr][nc][2] == num:
                    tmp_table[nr][nc].append((num, d))
                    break

    for r in range(1, n+1):
        for c in range(1, n+1):
            if not len(tmp_table[r][c]):
                table[r][c][0] = 0
                table[r][c][3] = None
            elif len(tmp_table[r][c]) == 1:
                table[r][c][0] = tmp_table[r][c][0][0]
                table[r][c][3] = tmp_table[r][c][0][1]
            else:
                winner = sorted(tmp_table[r][c])[0]
                table[r][c][0] = winner[0]
                table[r][c][3] = winner[1]




def minus_remain_seconds():
    for r in range(1, n+1):
        for c in range(1, n+1):
            if table[r][c][1] >= 1:
                table[r][c][1] -= 1

def is_one_remain():
    for r in range(1, n+1):
        for c in range(1, n+1):
            if table[r][c][0] >= 2:
                return False
    return True


def print_table():
    for r in range(1, n+1):
        for c in range(1, n+1):
            print(table[r][c], end = ' ')
        print()
    print("///////////////////")

second = 0
is_finished = False
while second < 1000:
    smell()
    second += 1
    move()
    minus_remain_seconds()
    if is_one_remain():
        is_finished = True
        break


if is_finished:
    print(second)
else:
    print(-1)


# 53m 소요