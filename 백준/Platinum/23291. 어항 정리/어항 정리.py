
n, k = map(int, input().split())

linear_bowls = list(map(int, input().split()))
linear_bowls.insert(0, -1)


def add_fish():
    min_fish = min(linear_bowls[1:])
    for i in range(len(linear_bowls)):
        if linear_bowls[i] == min_fish:
            linear_bowls[i] += 1


def first_stack_bowls():
    table_bowls = [[-1]*(n+1) for _ in range(n+1)]
    table_bowls[n-1][2] = linear_bowls[1]
    for i in range(2, n+1):
        table_bowls[n][i] = linear_bowls[i]
    h, w = 1, 1
    is_height = True
    cp = 1
    while True:
        cp += w
        if is_height:
            h += 1
            is_height = False
        else:
            w += 1
            is_height = True
        if cp+w+h-1 > n:
            break
        for r in range(1, h+1):
            for c in range(1, w+1):
                br = n-h+r
                bc = cp+c-1
                table_bowls[n-w+c-1][cp+w+h-r] = table_bowls[br][bc]
                table_bowls[br][bc] = -1
    return table_bowls


def is_there_bowls(table_bowls, r1, c1, r2, c2):
    return table_bowls[r1][c1] != -1 and table_bowls[r2][c2] != -1


def control_fish_number(table_bowls):
    tmp_bowls = [[0] * (n + 1) for _ in range(n + 1)]
    for r in range(1, n):
        for c in range(1, n+1):
            if not is_there_bowls(table_bowls, r, c, r+1, c):
                continue
            if table_bowls[r][c] >= table_bowls[r+1][c] + 5 :
                diff = (table_bowls[r][c]-table_bowls[r+1][c]) // 5
                tmp_bowls[r][c] -= diff
                tmp_bowls[r+1][c] += diff
            elif table_bowls[r+1][c] >= table_bowls[r][c] + 5:
                diff = (table_bowls[r+1][c]-table_bowls[r][c]) // 5
                tmp_bowls[r+1][c] -= diff
                tmp_bowls[r][c] += diff

    for r in range(1, n+1):
        for c in range(1, n):
            if not is_there_bowls(table_bowls, r, c, r, c+1):
                continue
            if table_bowls[r][c] >= table_bowls[r][c+1] + 5:
                diff = (table_bowls[r][c]-table_bowls[r][c+1]) // 5
                tmp_bowls[r][c] -= diff
                tmp_bowls[r][c+1] += diff
            elif table_bowls[r][c+1] >= table_bowls[r][c] + 5:
                diff = (table_bowls[r][c+1]-table_bowls[r][c]) // 5
                tmp_bowls[r][c+1] -= diff
                tmp_bowls[r][c] += diff

    for r in range(1, n+1):
        for c in range(1, n+1):
            table_bowls[r][c] += tmp_bowls[r][c]


def linearize(table_bowls):
    idx = 1
    for c in range(1, n+1):
        for r in range(n, 0, -1):
            if table_bowls[r][c] != -1:
                linear_bowls[idx] = table_bowls[r][c]
                idx += 1


def second_stack_bowls():
    table_bowls = [[-1]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        table_bowls[n][i] = linear_bowls[i]

    for i in range(1, n//2+1):
        table_bowls[n-1][n-i+1] = table_bowls[n][i]
        table_bowls[n][i] = -1

    for i in range(1, 1+n//4):
        table_bowls[n-2][n-i+1] = table_bowls[n-1][i+n//2]
        table_bowls[n-1][i+n//2] = -1
        table_bowls[n-3][n-i+1] = table_bowls[n][i+n//2]
        table_bowls[n][i+n//2] = -1

    return table_bowls

ans = 0
while True:
    ans += 1
    # 1. 물고기 한 마리 넣기
    add_fish()
    # 2. 어항 쌓기
    table = first_stack_bowls()
    # # 3. 물고기 수 조절
    control_fish_number(table)
    # # 4. 어항 일렬로 놓기
    linearize(table)
    # # 5. 다시 공중 부양
    table = second_stack_bowls()
    # # 6. 다시 물고기 조절
    control_fish_number(table)
    # 7. 다시 일렬로 놓기
    linearize(table)
    tmp_bowls = linear_bowls[1:]

    if max(tmp_bowls) - min(tmp_bowls) <= k:
        print(ans)
        break


