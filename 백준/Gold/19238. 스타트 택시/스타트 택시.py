from collections import deque

n, m, fuel = map(int, input().split())
table = [[None] * (n+1) for _ in range(n+1)]
blocks = [[False] * (n+1) for _ in range(n+1)]

for i in range(n):
    lst = list(map(int, input().split()))
    for j, val in enumerate(lst):
        if val == 1:
            blocks[i+1][j+1] = True

tr, tc = map(int, input().split())
for _ in range(m):
    sri, sci, ari, aci = map(int, input().split())
    table[sri][sci] = (ari, aci)

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

is_can_go = True

def in_range(nr, nc):
    return 0 < nr < n+1 and 0 < nc < n+1


def put_v(q, is_visited, vr, vc, parents, r, c, l):
    q.append((vr, vc, l))
    is_visited[vr][vc] = True
    parents[vr][vc] = (r, c)


def get_parent_route(parents, nr, nc, sr, sc):
    route = []
    while not (nr==sr and nc == sc):
        route.append((nr, nc))
        nr, nc = parents[nr][nc]
    return route[::-1]



def find_shortest_path(sr, sc, is_many, ar=0, ac=0):
    if is_many and table[sr][sc]:
        return None
    parents = [[False] * (n+1) for _ in range(n+1)]
    is_visited = [[False] * (n+1) for _ in range(n+1)]
    q = deque()
    put_v(q, is_visited, sr, sc, parents, -1, -1, 0)
    min_l = n**2
    maxes = []
    is_find = False
    while q and not is_find:
        vr, vc, l = q.popleft()
        for i in range(4):
            nr = vr + dr[i]
            nc = vc + dc[i]
            if not in_range(nr, nc) or blocks[nr][nc] or is_visited[nr][nc]:
                continue
            if (is_many and table[nr][nc]) or (not is_many and nr == ar and nc == ac):
                if l < min_l:
                    min_l = l
                    maxes = [(nr, nc)]
                elif l == min_l:
                    maxes.append((nr, nc))
                else:
                    is_find = True
                    break
            put_v(q, is_visited, nr, nc, parents, vr, vc, l+1)

    if maxes:
        maxes.sort()
        nr, nc = maxes[0]
        route = get_parent_route(parents, nr, nc, sr, sc)
        return route
    return None



def move(route):
    global tr, tc, fuel
    for r, c in route:
        if fuel <= 0:
            return False
        tr = r
        tc = c
        fuel -= 1
    return True


def move_to_guest():
    route = find_shortest_path(tr, tc, True)
    if route:
        return move(route), route[-1]
    elif table[tr][tc]:
        return True, (tr, tc)
    else:
        return False, (-1, -1)


def move_to_arrival(gr, gc):
    ar, ac = table[gr][gc]
    route = find_shortest_path(tr, tc, False, ar, ac)
    if not route:
        return False, 0
    table[gr][gc] = None
    return move(route), len(route)

for _ in range(m):
    is_can_go, (gr, gc) = move_to_guest()
    if not is_can_go:
        break
    is_can_go, used_fuel = move_to_arrival(gr, gc)
    if not is_can_go:
        break
    fuel += used_fuel * 2

if is_can_go:
    print(fuel)
else:
    print(-1)

