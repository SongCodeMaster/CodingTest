from itertools import permutations
# 현재 피로도에서 가능한 dungeongs 완전탐색 
# 어디부터 탐색해야되는거지? 
def solution(k, dungeons):
    answer = -1
    max_count = []
    for order in permutations(dungeons, len(dungeons)):
        count = 0
        current_k = k
        
        for min_use, use_k in order:
            if current_k >= min_use:
                current_k -= use_k
                count += 1
        max_count.append(count)
    
    return max(max_count)