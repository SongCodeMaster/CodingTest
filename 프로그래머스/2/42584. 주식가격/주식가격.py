def solution(prices):
    stack = []
    answer = [0]*len(prices)
    
    for i in range(len(prices)):

        while stack and stack[-1][1] > prices[i]:
            top_i, price = stack.pop()
            answer[top_i] = i - top_i
        
        stack.append((i,prices[i]))
    while stack:
        current_i, price = stack.pop()
        answer[current_i] = len(prices) - current_i - 1
        
    return answer