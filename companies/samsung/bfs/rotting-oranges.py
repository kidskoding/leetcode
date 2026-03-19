from collections import deque

def rottingOranges(grid):
    # let queue be a queue that holds the rotten oranges waiting to spread rot to their neighbors, level by level
    queue = deque()
    
    # let minutes be the total time elapsed until all oranges are rotten
    '''
    let fresh be the number of remaining fresh oranges after the rotting process
    if fresh > 0, then we know some oranges were unreachable during the rotting process, so we just return -1
    '''
    minutes, fresh = 0, 0
    
    # add all initially rotten oranges to queue, count fresh ones
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                queue.append((r, c))
            if grid[r][c] == 1:
                fresh += 1
        
    # 4 directions to spread the rotting: up, down, left, and right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue and fresh > 0:
        # go through each level of the queue one by one
        for _ in range(len(queue)):
            # get the row and column for the
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                # skip rotting for out of bounds or non-fresh calls
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] != 1:
                    continue
                
                # rot the neighbor and add to the next level
                grid[nr][nc] = 2
                
                # add the neighbor to the queue, since its orange is now rotted
                queue.append((nr, nc))
                
                # decrement the number of fresh oranges that remain
                fresh -= 1
        
        # a minute passes for each level in the queue
        minutes += 1
    
    # return the minutes if no fresh oranges remain, otherwise return -1
    return minutes if fresh == 0 else -1