from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    for order in permutations(dungeons, len(dungeons)):
        count = 0
        current_k = k
        for want_k, use_k in order:
            if current_k >= want_k:
                current_k -= use_k
                count += 1
            else:
                break
        
        max_count = max(max_count, count)
        
    return max_count