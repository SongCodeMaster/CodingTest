def merge_sort_count(arr):
    if len(arr) <= 1:
        return 0 # 역전쌍이 0개
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    
    inv = merge_sort_count(left) + merge_sort_count(right)

    i = j = k = 0

    # Merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else: 
            arr[k] = right[j]
            j += 1
            inv += (len(left) - i) # 왼쪽길이와 해당 인덱스를 빼서 역전쌍 세기
        k+= 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
    return inv

N = int(input())
A = list(map(int, input().split()))
print(merge_sort_count(A))