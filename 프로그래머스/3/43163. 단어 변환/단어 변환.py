from collections import deque
def one_diff(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count +=1

    if count == 1:
        return True
    else:
        return False
    
def solution(begin, target, words):
    if target not in words:
        return 0
    
    
    visited = {i:0 for i in words}
    
    q = deque()
    q.append((begin, 0))
    
    while q:
        current_word, current_dist = q.popleft()
        if current_word == target:
            return current_dist
        for next_word in words:
            if one_diff(current_word, next_word) and visited[next_word] == 0:
                visited[next_word] = 1
                q.append((next_word, current_dist+1))
        