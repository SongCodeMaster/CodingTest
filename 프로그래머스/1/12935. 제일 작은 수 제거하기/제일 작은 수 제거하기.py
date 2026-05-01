def solution(arr):
    if(len(arr) == 1):
        return [-1]
    
    delete_num = min(arr)
    answer = []
    
    for i in range(len(arr)):
        if arr[i] == delete_num:
            continue
        answer.append(arr[i])
        
    return answer