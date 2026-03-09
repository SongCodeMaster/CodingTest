# 흩어진 종이조각으로 소수를 만들 수 있는지
# 소수 받고 하나씩 쪼개서 보관해두고 결합하여 isPrime함수 만족하면 count += 1
# numbers 받고 하나씩 쪼개서 보관하면 시간복잡도가 너무 커지지않나? X

from itertools import permutations
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = 0
    my_num = list(numbers)
    my_answer = set()
    
    for i in range(1, len(my_num)+1):
        for p in permutations(my_num, i): # i=1, permutation(["1","7"],1)
            my_answer.add(int("".join(p))) # p는 ('1', ) 과같은 튜플
            
    count = 0
    
    for n in my_answer:
        if is_prime(n):
            count += 1
        
    return count
