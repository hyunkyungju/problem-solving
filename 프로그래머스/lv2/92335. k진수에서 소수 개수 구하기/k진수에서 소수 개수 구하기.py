def is_prime(num):
    for i in range(2, int(num ** (1/2)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    lst = list()
    knum = 0
    i = 0
    while n >= k:
        knum += (n % k) * pow(10, i)
        i += 1
        n //= k
    knum += n * pow(10, i)
    print(knum) 
    lst = str(knum).split('0')
    lst = [int(v) for v in lst if v ]
    answer = 0
    
    if not lst:
        return 0
    max_ = max(lst)
    
    if not max_ or max_ < 2:
        return 0

    for v in lst:
        if v > 1 and is_prime(v):
            answer += 1 
    
    return answer