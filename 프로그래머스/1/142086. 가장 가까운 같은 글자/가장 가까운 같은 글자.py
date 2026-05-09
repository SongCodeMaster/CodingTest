def solution(s):
    answer = []
    # 각 문자의 '마지막 위치'를 저장할 딕셔너리
    last_pos = {}
    
    # enumerate를 쓰면 인덱스와 글자를 동시에 가져온다
    for i, char in enumerate(s):
        if char in last_pos:
            # 현재위치 - 마지막 위치
            answer.append(i - last_pos[char])
        else:
            answer.append(-1)
        
        # 현재 글자의 위치를 딕셔너리에 업데이트
        last_pos[char] = i
        
    return answer