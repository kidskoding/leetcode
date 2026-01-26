def dfs(graph, node, visited):
    if visited[node]:  # already visited
        return
    visited[node] = True
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)

# DFS with cycle detection (useful for course schedule)
def dfs_cycle(graph, node, visited):
    if visited[node] == 1:  # visiting → found a cycle
        return False
    if visited[node] == 2:  # already visited
        return True
    visited[node] = 1  # mark as visiting
    for neighbor in graph[node]:
        if not dfs_cycle(graph, neighbor, visited):
            return False
    visited[node] = 2  # mark as visited
    return True