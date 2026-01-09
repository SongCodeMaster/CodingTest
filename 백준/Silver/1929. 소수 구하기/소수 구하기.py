# M과 N의 범위가 1,000,000인데 시간복잡도 N^2이면 상관없는건지

n, m = map(int, input().split())

num_list = [False, False] + [True]*(m)
prime_num = []
for i in range(2,m+1):
    if num_list[i]:
        prime_num.append(i)
        for j in range(2*i,m+1,i):
            num_list[j] = False

for i in prime_num:
    if n <= i and m >= i:
        print(i)