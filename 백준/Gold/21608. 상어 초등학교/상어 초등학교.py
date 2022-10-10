
n = int(input())
friends = [[] for _ in range( n**2 +1)]
childs = []
for _ in range(n**2):
    num, f, s, t, fo = map(int, input().split())
    friends[num] = (f, s, t, fo)
    childs.append(num)
rooms = [[-1] *(n+1) for _ in range(n+1)]


def in_range(r, c):
    return 1 <= r < n + 1 and 1 <= c < n + 1


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def count_friends_empty(r, c):
    friend_num = 0
    empty_num = 0
    for idx in range(4):
        nr = r + dr[idx]
        nc = c + dc[idx]
        if not in_range(nr, nc):
            continue
        if rooms[nr][nc] == -1:
            empty_num += 1
        else:
            for f in friends[child]:
                if rooms[nr][nc] == f:
                    friend_num += 1
                    break
    return friend_num, empty_num


for child in childs:
    max_f = 0
    max_e = 0
    lst = []

    # 친구가 인접한 칸에 가장 많은 곳, 비어있는 칸이 가장 많은 곳
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if rooms[r][c] != -1:
                continue
            f_num, e_num = count_friends_empty(r, c)
            if f_num > max_f or (f_num == max_f and e_num > max_e):
                lst = [(r, c)]
                max_f = f_num
                max_e = e_num
            elif f_num == max_f and e_num == max_e:
                lst.append((r, c))

    lst.sort()
    r, c = lst[0]
    rooms[r][c] = child



def get_nears():
    lst = []
    for idx in range(4):
        nr = r + dr[idx]
        nc = c + dc[idx]
        if not in_range(nr, nc):
            continue
        lst.append(rooms[nr][nc])
    return lst

ans = 0
for r in range(1, n+1):
    for c in range(1, n+1):
        child = rooms[r][c]
        fs = friends[child]
        nears = get_nears()
        friend_num = 0
        for near in nears:
            for friend in fs:
                if near == friend:
                    friend_num += 1
                    break
        if friend_num == 1:
            ans += 1
        elif friend_num == 2:
            ans += 10
        elif friend_num == 3:
            ans += 100
        elif friend_num == 4:
            ans += 1000
print(ans)

