import math

n, m = map(int, input().split())

size = m - n + 1 
num_TF = [True] * size

limit = int(math.isqrt(m)) 

for i in range(2, limit + 1):
    square = i * i  # 제곱수 (4, 9, 16...)
    
    # n // square는 몫. 딱 떨어지지 않으면 1을 더해 다음 배수
    start_index = n // square
    if n % square != 0:
        start_index += 1
        
    # 실제 시작하는 숫자 (예: min=10, sq=4 -> start_num=12)
    start_num = start_index * square
    
    # start_num부터 m까지 square 간격으로 점프하며 False 체크
    # j는 실제 숫자
    for j in range(start_num, m + 1, square):
        # 인덱스는 (실제 숫자 - n)으로 매핑
        num_TF[j - n] = False

# True(제곱ㄴㄴ수)인 것의 개수 출력
print(sum(num_TF))