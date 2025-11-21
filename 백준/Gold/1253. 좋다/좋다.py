import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
A.sort()

count = 0
for k in range(n):
        i = 0
        j = n-1
        good_num = A[k]

        while i < j:
            result = A[i] + A[j]

            if result == good_num:
                  if i != k and j != k:
                        count += 1
                        break
                  elif i == k:
                    i+=1
                  else:
                    j-=1
                  
            elif result > good_num:
                  j -= 1
            else: 
                i+=1
print(count)