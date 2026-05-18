from collections import deque
def diff_word(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    
    if count == 1:
        return True
    else:
        return False
    
def solution(begin, target, words):
    answer = 0
    visited = { i: 0 for i in words }
    
    q = deque()
    q.append((begin, 0))
    visited[begin] = 1
    
    while q:
        current_word, dist = q.popleft()
        
        if current_word == target:
            return dist
        
        for next_word in words:
            if visited[next_word] == 0 and diff_word(current_word, next_word):
                visited[next_word] = 1
                q.append((next_word, dist + 1))
        
    return 0