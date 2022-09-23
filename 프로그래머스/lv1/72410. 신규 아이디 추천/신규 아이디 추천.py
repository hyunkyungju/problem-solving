def solution(new_id):
    ips = list(new_id)
    ers = list("~!@#$%^&*()=+[{]}:?,<>/")
    
    for i, c in enumerate(ips):
        if 65 <= ord(c) and ord(c) <= 90:
            ips[i] = chr(ord(c)+32)
        elif c in ers:
            ips[i] = ''
    
    ips = list(''.join(ips))
    for i in range(len(ips) - 1):
        if ips[i] == '.' and ips[i+1] == '.':
            j = i + 1
            while j < len(ips) and ips[j] == '.':
                ips[j] = ''
                j += 1
    answer = ''.join(ips)
    print(answer)
    if len(answer) >= 1 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) >= 1 and answer[-1] == '.':
        answer = answer[:-1]    
    if not len(answer):
        answer = "a"
    print(answer)
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[14] == '.':
            tmps = list(answer)
            tmps[14] = ''
            answer = ''.join(tmps)
    while len(answer) <= 2:
        answer = answer + answer[-1]

    return answer
