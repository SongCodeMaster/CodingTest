def solution(tickets):
    tickets.sort(reverse=True)
    print(tickets)
    graph = {}
    
    for start, end in tickets:
        if start not in graph:
            graph[start] = []
        graph[start].append(end)
    
    stack = ["ICN"]
    path = []
    
    while stack:
        top = stack[-1]
        
        if top in graph and len(graph[top]) > 0:
            next_airplain = graph[top].pop()
            stack.append(next_airplain)

        else:
            path.append(stack.pop())
    
    return path[::-1]
            
    answer = []
    return answer