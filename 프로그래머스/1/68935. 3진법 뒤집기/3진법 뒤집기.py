def solution(n):
    three_num = ''
    while n > 0:
        three_num += str(n % 3)
        n = n // 3

    return int(three_num, 3)