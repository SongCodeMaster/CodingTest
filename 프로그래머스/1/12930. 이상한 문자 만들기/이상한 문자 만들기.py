def solution(s):
    answer = []
    s = s.split(' ')
    
    for i in s:
        my_string = ''
        for index, string in enumerate(i):
            if index % 2 == 0:
                my_string += string.upper()
            else:
                my_string += string.lower()
        answer.append(my_string)

    return ' '.join(answer)