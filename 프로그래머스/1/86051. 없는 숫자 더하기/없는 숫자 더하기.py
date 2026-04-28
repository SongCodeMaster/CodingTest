def solution(numbers):
    answer = [False]*(10)
    sum = 0
    
    for i in range(len(numbers)):
        array_number = numbers[i]
        answer[array_number] = True
    
    for i in range(len(answer)):
        if answer[i] == False:
            sum += i
    return sum