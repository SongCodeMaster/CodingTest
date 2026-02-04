# 색종이 붙이기
# 구현문제다 즉, 색칠하기 문제임
n = int(input())
mat = [[0]*100 for _ in range(100)]

for i in range(n):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            mat[x+j][y+k] = 1

count = 0
for i in range(100):
    for j in range(100):
        if mat[i][j] == 1:
            count += 1

print(count)