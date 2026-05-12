def solution(phone_book):
    phone_set = set(phone_book)
    
    for i in phone_book:
        separate = ''
        for j in range(len(i)-1):
            separate += i[j]
            if separate in phone_set:
                return False

    return True