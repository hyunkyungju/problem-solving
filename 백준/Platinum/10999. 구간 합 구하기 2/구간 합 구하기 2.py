import math

N = 0
tree = []
lazys = []
SQUARE = 0

def sol():
    global N, SQUARE, tree, lazys
    n, m, k = map(int, input().split())
    square = 1 << math.ceil(math.log(n, 2))
    N, SQUARE = n, square
    tree = [0] * (2*square)
    lazys = [0] * (2*square)
    for i in range(square, square + n):
        tree[i] = int(input())
    for i in range(square-1, 0, -1):
        tree[i] = tree[i*2] + tree[i*2+1]
    for _ in range(m+k):
        a, *q = map(int, input().split())
        if a == 1:
            b, c, d = q
            update(b-1, c-1, d, 1, 0, square-1)
        else:
            b, c = q
            ans = query(b-1, c-1, 1, 0, square-1)
            print(ans)


def update(left, right, change, idx, start, end):
    update_lazy(idx, start, end)

    if start > right or end < left:
        return
    # 아예 들어간 경우
    if left <= start and end <= right:
        lazys[idx] = change
        update_lazy(idx, start, end)
        return
    update(left, right, change, idx*2, start, (start+end)//2)
    update(left, right, change, idx*2 + 1, (start+end)//2 + 1, end)
    tree[idx] = tree[idx*2] + tree[idx*2 + 1]


def update_lazy(idx, start, end):
    val = lazys[idx]
    if not val:
        return
    end = min(end, N-1)
    tree[idx] += (end-start+1)*val
    if start != end:
        lazys[idx*2] += val
        lazys[idx*2 + 1] += val
    lazys[idx] = 0


def query(left, right, idx, start, end) -> int:
    update_lazy(idx, start, end)

    if start > right or end < left:
        return 0
    # 아예 들어간 경우
    if left <= start and end <= right:
        return tree[idx]
    lans = query(left, right, idx*2, start, (start+end)//2)
    rans = query(left, right, idx*2 + 1, (start+end)//2 + 1, end)
    return lans + rans


sol()
