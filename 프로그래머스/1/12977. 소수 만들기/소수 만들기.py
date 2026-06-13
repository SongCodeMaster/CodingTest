from itertools import combinations
def is_prime(n):
    for i in range(2,n // 2):
        if n % i == 0:
            return False
    
    return True
    
    
def solution(nums):
    answer = 0
    com_list = list(combinations(nums,3))
    
    for i in com_list:
        if is_prime(sum(i)):
            answer += 1
    
    return answer