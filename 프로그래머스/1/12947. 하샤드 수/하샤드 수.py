def solution(x):
    divide_num = 0
    for i in str(x):
        divide_num += int(i)
        
    if x % divide_num == 0:
        return True
    else:
        return False