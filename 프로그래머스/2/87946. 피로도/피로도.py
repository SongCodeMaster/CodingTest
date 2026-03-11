visited = []
answer = 0

def dfs(HP, dungeons, count):
    global answer
    
    if answer < count:
        answer = count
    
    for i in range(len(dungeons)):
        if not visited[i] and dungeons[i][0] <= HP:
            visited[i] = True
            dfs(HP - dungeons[i][1], dungeons, count + 1)
            visited[i] = False
    
def solution(k, dungeons):
    global answer, visited
    
    visited = [False for _ in range(len(dungeons))]
    dfs(k,dungeons, 0)
    
    return answer