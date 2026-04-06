def dfs(numbers,target,sum,idx):
    global count
    
    if idx == len(numbers):
        if target == sum:
            count += 1
        return
            
    
    
    # 빼기 dfs
    dfs(numbers, target, sum + numbers[idx], idx+1)
    # 더하기 dfs
    dfs(numbers, target, sum - numbers[idx], idx+1)
    
    
def solution(numbers, target):
    global count
    count = 0 
    sum = 0
    
    dfs(numbers, target, sum, 0)
    return count