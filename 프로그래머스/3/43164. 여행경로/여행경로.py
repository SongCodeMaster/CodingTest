def solution(tickets):
    tickets.sort(reverse=True)
    
    graph = {}
    stack = ["ICN"]
    path = []
    
    for a,b in tickets:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        
    while stack:
        top = stack[-1]
        
        if top in graph and len(graph[top]) > 0:
            next_travle = graph[top].pop()
            stack.append(next_travle)
        else:
            path.append(stack.pop())
            
    return path[::-1]
        