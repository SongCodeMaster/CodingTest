def solution(s):
    answer = []
    my_word = s.split(' ')
    
    for i in my_word:
        my_answer = ''
        for index, word in enumerate(i):
            if index % 2 == 0:
                my_answer += word.upper()
            else:
                my_answer += word.lower()
                
        answer.append(my_answer)
    
    return ' '.join(answer)