from collections import deque
# n1: begin, n2: words
def diff_one(n1, n2):
    count = 0
    for i in range(len(n2)):
        if n1[i] != n2[i]:
            count += 1
        if count >= 2:
            return False
    
    if count == 1:
        return True
    
# 딕셔너리로 저장하여 BFS 처리
def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    visited = {i:0 for i in words}
    visited[begin] = 0
    
    q = deque()
    q.append(begin)
    
    while q:
        current_word = q.popleft()
        if current_word == target:
            return visited[current_word]
        
        for next_word in words:
            if visited[next_word] == 0 and diff_one(current_word, next_word):
                    
                current_dist = visited[current_word] 
                visited[next_word] = current_dist + 1
                q.append(next_word)



