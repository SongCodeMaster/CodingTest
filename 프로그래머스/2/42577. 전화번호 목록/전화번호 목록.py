def solution(phone_book):
    answer = True

    book_set = set(phone_book)
    
    for word in phone_book:
        separate = ''
        for i in range(len(word) - 1):
            separate += word[i]
            if separate in book_set:
                return False
            
    return True