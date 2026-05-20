from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    for order in permutations(dungeons, len(dungeons)):
        current_k = k
        count = 0
        for dungeon_k, use_k in order:
            if current_k >= dungeon_k:
                current_k -= use_k
                count += 1
            else:
                break
            
        max_dungeons = max(max_dungeons, count)
            
    return max_dungeons