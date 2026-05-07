def solution(number):
    answer = 0
    result = 0
    for i in range(0, len(number)):
        for j in range(1, len(number)):
            if i >= j:
                continue
            for k in range(2, len(number)):
                if j >= k or i >= k:
                    continue
                answer = number[i] + number[j] + number[k]
                if answer == 0:
                    result += 1
                else:
                    answer = 0
                
    return result