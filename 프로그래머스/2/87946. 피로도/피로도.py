from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    
    for order in permutations(dungeons, len(dungeons)):
        current_k = k
        count = 0
        
        for min_k, use_k in order:
            if current_k >= min_k:
                current_k -= use_k
                count += 1
            else:
                break # 더 이상 불가하면 현재 순서 종료
        
        # 해당 순서 마무리되면 값 갱신해주기
        max_dungeons = max(max_dungeons, count)
            
    
    return max_dungeons