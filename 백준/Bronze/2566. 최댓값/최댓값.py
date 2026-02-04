# 최댓값과 위치 출력하기, 이차원 배열문제
mat = [ list(map(int, input().split())) for _ in range(9)]

my_max = 0
my_i = 0
my_j = 0
result = [0,0]
for i in range(9):
    for j in range(9):
        if my_max <= mat[i][j]:
            my_max = mat[i][j]

            my_i = i
            my_j = j
            result[0] = i + 1
            result[1] = j + 1

print(my_max)
print(*result)