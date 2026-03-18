def numberOfIslands(grid):
    # check if the grid is empty. we cannot traverse an empty grid
    if not grid:
        return 0
    
    # let islandCount be the number of islands in the grid
    islandCount = 0
    
    # let rows and cols be the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])
    
    # use depth first search (DFS) to traverse the grid
    def dfs(r, c):
        # check if the current row is out of bounds or the current column is out of bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        
        # check if the current cell is water. if it is, we cannot traverse it, since we only want to traverse land
        if grid[r][c] == '0':
            return
        
        # sink the current land by marking the current cell as visited by setting it to water (0)
        # this is because we do not want to traverse the same cell twice
        grid[r][c] = '0'
        
        # recursively traverse the four adjacent cells
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    # traverse the grid
    for r in range(rows):
        for c in range(cols):
            # check if the current cell is land, and if so add it to the island count
            if grid[r][c] == '1':
                islandCount += 1
                
                # perform dfs on neighbors (top, bottom, left, right)
                dfs(r, c)
                
    # return the number of islands
    return islandCount