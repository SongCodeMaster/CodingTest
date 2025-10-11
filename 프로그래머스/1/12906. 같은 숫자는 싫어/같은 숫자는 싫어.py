def solution(arr):
    # O(n) 풀이
    if not arr:
        return []
    
    answer = [arr[0]] # 첫 요소는 무조건 포함
    
    for num in arr[1:]:
        if num != answer[-1]: # 이전 값과 다르면 append
            answer.append(num)
            
    return answer