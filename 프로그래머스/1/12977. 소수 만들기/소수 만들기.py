from itertools import combinations

def is_prime(num):
        for i in range(2, num // 2):
            if num % i == 0:
                return False
        
        return True
    
def solution(nums):
    answer = 0
    nums = combinations(nums, 3)
        
    for number in list(nums):
        result = sum(number)

        if is_prime(result) == True:
            answer += 1

    return answer