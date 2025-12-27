import sys
input = sys.stdin.readline
n=int(input())

number = [0]*n
for i in range(n):
    number[i] = int(input())

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubble_sort(number)

for i in range(n):
    print(number[i])