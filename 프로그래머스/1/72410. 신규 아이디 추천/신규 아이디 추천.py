def solution(new_id):
    # 1: 소문자 치환
    answer = new_id.lower()
    
    # 2단계
    for i in answer:
        if i.islower() or i.isdigit() or i == '.' or i == '-' or i == '_':
            continue
        else:
            answer = answer.replace(i,"")
    
    # 3단계
    while(".." in answer):
        answer = answer.replace("..",".")
        
    # 4단계
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    
    # 5단계
    if len(answer) == 0:
        answer += 'a'
        
    # 6단계
    count = 0
    if len(answer) >= 16:
        for i in answer:
            count += 1
        
            if count > 15:
                answer = answer[:15]
                if answer[14] == '.':
                    answer = answer[:14]
                break

    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer = answer + answer[-1]
    
    return answer