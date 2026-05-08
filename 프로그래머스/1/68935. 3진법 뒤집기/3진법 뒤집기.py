# 3진법으로 바꾸기 -> 앞뒤 반전시키기 -> 10진법으로 표현하기
def solution(n):
    three_str = ""
    while n > 0:
        # n을 3으로 나눈 나머지를 뒤에 붙이면 자연스럽게 '앞뒤 반전'된 3진법 생성
        three_str += str(n % 3)
        n //= 3
        
    return int(three_str, 3)