from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    visited = set()
    
    while q:
        current_word, step = q.popleft()
        
        if current_word == target:
            return step
        
        # words에 있는 단어 중 변환 가능한 단어 찾기
        for word in words:
            if word not in visited:
                # 한글자만 다르면 수행
                diff = sum(1 for a, b in zip(current_word, word) if a != b)
                
                if diff == 1:
                    visited.add(word)
                    q.append((word, step + 1))
    
    answer = 0
    return answer