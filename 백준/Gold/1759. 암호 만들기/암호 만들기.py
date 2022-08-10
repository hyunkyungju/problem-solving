import sys
import itertools

input = sys.stdin.readline

l, c = map(int, input().split())
ips = sorted(list(input().split()))


def is_pass(lst):
    moem = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for al in moem:
        if al in lst:
            cnt += 1
    if cnt >= 1 and l - cnt >= 2:
        return True
    return False


def bt(s):
    if len(s) == l:
        if is_pass(s):
            print(''.join(s))
        return
    for v in ips[ips.index(s[-1]) + 1:]:
        bt(s + [v])


for i in range(c - 3):
    bt([ips[i]])
