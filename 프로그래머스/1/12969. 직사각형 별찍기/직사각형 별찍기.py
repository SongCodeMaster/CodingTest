a, b = map(int, input().strip().split(' '))

while b != 0:
    for _ in range(a):
        print('*',end='')
    print()
    b -= 1