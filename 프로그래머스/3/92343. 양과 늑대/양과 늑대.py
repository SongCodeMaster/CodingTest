# 상태 
def solution(info, edges):
    answer = 0
    tree = [[] for _ in range(len(info))]
    sheep = 0
    wolves = 0
    
    for u, v in edges:
        tree[u].append(v)
    
    def dfs(current_node, sheep, wolves, next_nodes):
        nonlocal answer
        
        # 현재 노드에 있는 동물 파악하여 마리 증가
        if info[current_node] == 0:
            sheep += 1
        else:
            wolves += 1
        
        if sheep <= wolves:
            return
        
        # 잡아 먹히지 않으면 최댓값 갱신
        answer = max(answer, sheep)
        
        # 이용가능한 노드 추가
        # 현재 노드는 방문 -> 목록에서 제거
        # 자식 노드들 추가하기
        available_nodes = next_nodes[:]
        available_nodes.remove(current_node)
        for child in tree[current_node]:
            available_nodes.append(child)
            
        # 순회
        for next in available_nodes:
            dfs(next, sheep, wolves, available_nodes)
            print(available_nodes)
    
    # 초기: 0번 노드 방문, 양 0, 늑대 0, 갈 수 있는 후보 [0]
    dfs(0,0,0,[0])
    
    return answer