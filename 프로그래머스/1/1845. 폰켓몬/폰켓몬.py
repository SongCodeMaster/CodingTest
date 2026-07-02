def solution(nums):
    nums.sort()  
    
    unique_count = 1 
    max_pick = len(nums) // 2
    
    if unique_count == max_pick:
        return max_pick
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            unique_count += 1
            
            if unique_count == max_pick:
                return max_pick
            
    return unique_count