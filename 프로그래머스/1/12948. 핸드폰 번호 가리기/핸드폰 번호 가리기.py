def solution(phone_number):
    my_list = list(map(str,phone_number))
    print(my_list)
    for i in range(0,len(phone_number)-4):
        my_list[i] = '*'
        
    return "".join(my_list)