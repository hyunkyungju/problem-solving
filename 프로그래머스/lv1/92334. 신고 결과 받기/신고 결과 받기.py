
from collections import defaultdict
def solution(id_list, report, k):
    list_dict = defaultdict(list)
    answer = [0] * len(id_list)
    report_set = set(report)
    for r in report_set:
        caller, callee = map(str, r.split())
        list_dict[callee].append(caller)

    for key, value in list_dict.items(): 
        if len(value) < k :
            continue
        for name in value:
            answer[id_list.index(name)] += 1                
    

    return answer