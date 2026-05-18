def solution(prices):
    # (주식값, 인덱스)
    stack = []
    result = [0] * (len(prices))
    
    for i in range(len(prices)):
        while stack and stack[-1][0] > prices[i]:
            value, index = stack.pop()
            result[index] = i - index
        
        stack.append((prices[i], i))
    
    while stack:
        value, index = stack.pop()
        result[index] = len(prices) - 1 - index
        
    return result