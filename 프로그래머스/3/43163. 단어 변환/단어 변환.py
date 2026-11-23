from collections import deque
# 최단거리로 가는 경우 얘기하는거면 재귀방식? BFS? 덱에 넣어두고 문제풀이 수행해보자. 
def one_diff(f, s):
    count = 0
    for i in range(len(f)):
        if f[i] != s[i]:
            count += 1

    if count == 1:
        return True
    else:
        return False
    
    
def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = { i: False for i in words }
    q = deque()
    q.append((begin, 0))
    
    while q:
        curr_word, dist = q.popleft()
        
        if curr_word == target:
            return dist
        
        for next_word in words:
            if one_diff(curr_word, next_word) and not visited[next_word]:
                visited[next_word] = True
                q.append((next_word, dist+1))
        
    
    return 0