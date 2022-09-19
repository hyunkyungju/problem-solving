def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** (1/2)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    word = ""
    while n:
        word = str(n % k) + word 
        n //= k
    print(word) 
    lst = [int(v) for v in word.split('0') if v ]
    answer = 0

    for v in lst:
        if is_prime(v):
            answer += 1 
    
    return answer