def solution(prices):
    answer = [0] * (len(prices))
    stack = []
    
    for i in range(len(prices)):
        while stack and stack[-1][0] > prices[i]:
            value, index = stack.pop()
            answer[index] = i-index
        
        stack.append((prices[i], i))
        
    while stack:
        value, index = stack.pop()
        answer[index] = len(prices) - 1 - index 
        
    return answer