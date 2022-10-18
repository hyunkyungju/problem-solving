
t = int(input())
for idx in range(t):
    n, k = map(int, input().split())
    l = n // 4
    lst = []
    numbers = input()
    for _ in range(l):
        for i in range(4):
            s = str(numbers[i*l:(i+1)*l])
            lst.append(s)
        numbers = numbers[-1]+numbers[:-1]
    lst = list(set(lst))
    lst.sort(reverse=True)
    ans_d = lst[k-1]
    ans = int(ans_d, 16)
    print(f"#{idx+1} {ans}")