from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True
    
def solution(numbers):
    answer = 0
    visited = set()
    for i in range(1, len(numbers)+1):
        for order in permutations(numbers, i):
            result = int(''.join(order))
            
            visited.add(result)
    
    for i in visited:
        if is_prime(i):
            answer += 1
    
    return answer