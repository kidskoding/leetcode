from collections import deque

def rottingOranges(grid):
    # let minutes be the number of minutes that has elapsed until no cell has a fresh orange
    minutes = 0
    
    # let queue be the order that the oranges are visited in
    queue: deque = deque()
    
    # let fresh track fresh oranges so we can detect unreachable ones at the end
    fresh = 0

    # add all initially rotten oranges to queue, count fresh ones
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    
    # use bfs to process one full level per minute
    # at each level, all oranges that are fresh and next to a rotting orange rot at the same time            
    while queue:
        # process the current level of the queue
        for _ in range(len(queue)):
            r, c = queue.popleft()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # if out of bounds, skip the rot
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                
                # rot fresh neighbor, add to queue for next level
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
            
            # one full level done = one minute elapsed
            minutes += 1
    
    # if fresh > 0, some oranges were unreachable and could not be rotted, so we just return -1
    return minutes if fresh == 0 else -1