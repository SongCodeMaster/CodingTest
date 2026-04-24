def solution(n):
    x = n ** (1/2)
    if n % x == 0:
        return (x+1) * (x+1)
    else:
        return -1 