def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[0])):
            result = arr1[i][j] + arr2[i][j]
            row.append(result)
        answer.append(row)
            
    return answer