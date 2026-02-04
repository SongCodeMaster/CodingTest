# 2차원 배열
# 행은 출력 가능한데 열의 인덱스를 가져오는거 고려해야한다.
# 열의 인덱스는....
# 5개의 단어 (행은 5번)

words = [[] for _ in range(5)]

words = [ list(input()) for _ in range(5)]

max_index = 0
for i in range(5):
    my_max = len(words[i])
    if max_index < my_max:
        max_index = my_max

for j in range(max_index):
    for k in range(5):
        if j < len(words[k]):
            print(words[k][j], end = "")
