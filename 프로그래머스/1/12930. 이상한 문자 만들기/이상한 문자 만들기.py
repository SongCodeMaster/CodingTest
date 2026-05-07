def solution(s):
    answer = []
    words = s.split(' ')
    
    for word in words:
        converted = ''
        for i in range(len(word)):
            if i % 2 == 0:
                converted += word[i].upper()
            else:
                converted += word[i].lower()
        answer.append(converted)
    
    return ' '.join(answer)