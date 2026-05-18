# 소수니까, n을 반복문으로 is_prime함수 써서 찾으면? 시간초과.
# 숫자 자체를 가능성 트리로 만들어서 완전 탐색 진행하면 된다.
# 에라토스테네스의 체? 그거쓰면 되나. 그게 탐색공간을 정의하고 그 배수들 전부 지운다음에 남은 애들 소수 반환하는것 아닌가.
# 탐색 공간들을 T/F로 나타내야한다.
def solution(n):
    prime_list = []
    number_list = [False, False] + [True] * (n-1)
    
    for i in range(2, n+1):
        if number_list[i]:
            prime_list.append(i)
            for j in range(2*i, n+1, i):
                number_list[j] = False
    
    return len(prime_list)