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

# DFS on a grid
def dfs(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return
    if grid[r][c] != '1':
        return
    
    grid[r][c] = '0'
    dfs(grid, r+1, c)
    dfs(grid, r-1, c)
    dfs(grid, r, c+1)
    dfs(grid, r, c-1)