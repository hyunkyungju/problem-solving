from itertools import combinations
from collections import defaultdict

def is_in(tmps, order): #('A', 'B', 'C')
    i = 0
    for v in sorted(list(order)):
        if tmps[i] == v:
            i += 1
            if i == len(tmps):
                return True
        elif tmps[i] < v:
            return False
    return False
    
def solution(orders, course):
    answer = []
    menus = []
    for order in orders:
        menus.extend(list(order))
    menus = sorted(list(set(menus)))
    for n in course:
        com_dict = defaultdict(int)
        for order in orders:
            coms = list(combinations(sorted(list(order)), n))
            for tmps in coms:
                tmp = ''.join(tmps)
                com_dict[tmp] += 1
        if not len(com_dict):
            continue
        max_ordered = max(com_dict.values())
        if max_ordered >= 2: 
            max_list = [''.join(key) for key, val in com_dict.items() if val == max_ordered]
            answer.extend(max_list)
    answer.sort()
    return answer
'''
def solution(orders, course):
    answer = []
    menus = []
    for order in orders:
        menus.extend(list(order))
    menus = sorted(list(set(menus)))
    for n in course:
        coms = list(combinations(menus, n))
        com_dict = dict()
        for tmps in coms: 
            cnt = 0
            for order in orders: 
                if is_in(tmps, order):
                    cnt += 1
            com_dict[tmps] = cnt
        max_ordered = max(com_dict.values())
        if max_ordered >= 2: 
            max_list = [''.join(key) for key, val in com_dict.items() if val == max_ordered]
            answer.extend(max_list)
    answer.sort()
    return answer


'''