def solution(n, info):
    num_list = [[0] * (n + 1) for _ in range(11)] 
    lst_list = [[[] for _ in range(n+1)] for _ in range(11)]
    for i in range(11):
        target = 10-i
        value = target
        apeach_shoot = info[i]
        if apeach_shoot:
            value *= 2
        lion_shoot = apeach_shoot + 1
        
        if lion_shoot > n:
            if i == 0:
                continue
            for j in range(n + 1):
                num_list[i][j] = num_list[i-1][j]
                lst_list[i][j] = lst_list[i-1][j][:]
            continue
        
            
            
        if i == 0:
            num_list[0][lion_shoot] = value
            lst_list[0][lion_shoot].append(target)
            continue
                
        for j in range(lion_shoot):
            num_list[i][j] = num_list[i-1][j]
            lst_list[i][j] = lst_list[i-1][j][:]
        for j in range(lion_shoot, n + 1):
            if j != lion_shoot and num_list[i-1][j - lion_shoot] == 0 and num_list[i-1][j] == 0:
                continue
            if num_list[i-1][j - lion_shoot] + value >= num_list[i-1][j]:
                num_list[i][j] = num_list[i-1][j - lion_shoot] + value
                lst_list[i][j] = lst_list[i-1][j - lion_shoot][:]
                lst_list[i][j].append(target)
            else:
                num_list[i][j] = num_list[i-1][j]
                lst_list[i][j] = lst_list[i-1][j][:]
    max_ = max(num_list[n])
    tmp = []
    for i in range(n+1):
        if num_list[n][i] == max_:
            tmp.append(lst_list[n][i])
    print(tmp)
    #tmp.sort(key = lambda x: (-sum(x), -len(x)))
    lst = tmp[0]
    
    lion_score = sum(lst)
    apeache_score = 0
    for i in range(11):
        if i not in lst and info[10-i]:
            apeache_score += i
    if lion_score <= apeache_score:
        return [-1]
    
    answer = [0] * 11
    for i in range(11):
        if i in lst:
            answer[10-i] = info[10-i] + 1
    answer[10] = n-sum(answer)
    return answer