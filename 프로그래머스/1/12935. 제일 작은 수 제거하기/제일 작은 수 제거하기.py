def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    min_value = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
    arr.remove(min_value)
    return arr