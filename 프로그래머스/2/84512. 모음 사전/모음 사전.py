def solution(word):
    answer = 0
    words = []
    alphabet = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(current_word):
        if len(current_word) > 5:
            return 
        
        if current_word:
            words.append(current_word)
        
        for a in alphabet:
            dfs(current_word + a)
    
    dfs("")
    
    return words.index(word) + 1