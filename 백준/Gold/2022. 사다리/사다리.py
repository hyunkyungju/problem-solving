import sys
import math

input = sys.stdin.readline

x, y, c = map(float, input().split())

lo = 0
hi = min(x, y)


def f(w):
    h1 = math.sqrt(pow(x, 2) - pow(w, 2))
    h2 = math.sqrt(pow(y, 2) - pow(w, 2))
    c = (h1 * h2) / (h1 + h2)
    return c


ans = 0
while (hi - lo) > 0.000001:
    mid = (lo + hi) / 2
    f_c = f(mid)
    ans = mid
    if f_c >= c:    
        lo = mid
    else:
        hi = mid
print(ans)

