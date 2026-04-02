count = 0

def dfs(numbers,target,idx,value):
    global count
    if len(numbers) == idx:
        if value == target:
            count += 1
        return
            
    dfs(numbers,target,idx+1, value + numbers[idx])
    dfs(numbers,target,idx+1, value - numbers[idx])
    
def solution(numbers, target):
    global count
    count = 0
    dfs(numbers,target,0,0)
    return count