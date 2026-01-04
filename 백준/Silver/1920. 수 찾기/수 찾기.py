n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
B = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            print(1)
            return 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(0)


for i in range(m):
    binary_search(A, B[i])