def floodFill(image, sr, sc, color):
    # save the original color before we start changing anything
    original = image[sr][sc]
    
    # early return if already the target color — avoids infinite loop
    if original == color:
        return image
    
    # DFS because we need to explore all connected pixels from a starting point
    # we go deep in one direction until we hit a boundary or wrong color, then backtrack
    # Time: O(M*N) — we visit every pixel at most once
    # Space: O(M*N) — recursive call stack in worst case (entire grid is one color)
    def dfs(r, c):
        # stop if out of bounds
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
            return
        
        # stop if not original color — wrong cell or already visited
        if image[r][c] != original:
            return
        
        # recolor and explore all 4 directions
        image[r][c] = color
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    dfs(sr, sc)
    return image