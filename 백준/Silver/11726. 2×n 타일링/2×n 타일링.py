# 타일 채우기

n = int(input())
mod = 10007
A = [0]*(n+2)
A[1] = 1
A[2] = 2
for i in range(3,n+1):
    A[i] = (A[i-1] + A[i-2]) % mod
    
print(A[n])