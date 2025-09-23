from collections import defaultdict

# Create a graph in the form of a dictionary
graph = defaultdict(list)

# Can be any number for n, depending on problem
n = 10 
visited = [0] * n

def dfs(node):
    if visited[node] == 1:
        return False
    if visited[node] == 2:
        return True
    
    visited[node] = 1
    for neighbor in graph[node]:
        if not dfs(neighbor):
            return False
        
    visited[node] = 2
    return True
