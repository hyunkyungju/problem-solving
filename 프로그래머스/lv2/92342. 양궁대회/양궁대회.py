max_ = 0
max_shoots = [0] * 11

def change_max(new_max, new_max_shoots):
    global max_
    global max_shoots
    max_ = new_max
    max_shoots = new_max_shoots[:]
    
def get_score_diff(ap_shoots, lion_shoots):
    ap_score = 0
    lion_score = 0
    for i in range(10):
        target_score = 10 - i
        if ap_shoots[i] == 0 and lion_shoots[i] == 0:
            continue
        if ap_shoots[i] >= lion_shoots[i]:
            ap_score += target_score
        else:
            lion_score += target_score
    print("diff:", lion_score - ap_score, lion_shoots)
    return lion_score - ap_score
    
    
def dfs(info, shoots, remain_shoot, target):
    if target == 0:
        shoots[10] = remain_shoot
        score_diff = get_score_diff(info, shoots)
        if score_diff > max_:
            change_max(score_diff, shoots)
        elif score_diff == max_:
            current_max_point = 0
            new_max_point = 0
            for i in range(11):
                current_max_point += pow(10, i) * max_shoots[i]
                new_max_point += pow(10, i) * shoots[i]
            print("cr:", current_max_point, "shoots:", max_shoots )
            print("new:", new_max_point, "shoots:", shoots )
            if new_max_point > current_max_point:
                change_max(score_diff, shoots)
        return
    ap_shoot = info[10 - target] 
    new_shoots = shoots[:]
    dfs(info, new_shoots, remain_shoot, target - 1)
    if remain_shoot >= ap_shoot + 1:
        lion_shoot = ap_shoot + 1
        new_shoots[10 - target] = lion_shoot
        dfs(info, new_shoots, remain_shoot - lion_shoot, target - 1)
    
    

def solution(n, info):
    
    dfs(info, [0] * 11 , n, 10)
    
    
    answer = max_shoots
    if max_ == 0:
        answer = [-1]
    return answer