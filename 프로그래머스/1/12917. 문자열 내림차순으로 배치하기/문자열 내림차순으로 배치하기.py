def solution(s):
    new_string = sorted(list(s), reverse=True)
    return ''.join(new_string)
