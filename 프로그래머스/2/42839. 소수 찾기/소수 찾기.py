from itertools import permutations
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    
    return True
    

def solution(numbers):
    answer = 0
    result = set()
    
    for j in range(1,len(numbers)+1):
        for i in permutations(numbers, j):
            num = int("".join(i))
            if num >= 2 and is_prime(num):
                result.add(num)
    
    for i in result:
        answer += 1
    
    return answer