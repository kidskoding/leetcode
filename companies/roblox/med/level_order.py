from typing import Optional
from base.treenode import TreeNode
from collections import deque

# Time: O(n) processing n nodes at a time per iteration
# Space: O(n) because queue holds at most one full level of nodes
# at the widest point the queue can contain n/2 nodes (last level of balanced tree)
def levelOrder(root: Optional[TreeNode]):
    if not root:
        return []
    
    queue = deque([root])
    res = []
    
    while queue:
        n = len(queue)
        curr_level = []
        
        for _ in range(n):
            node = queue.popleft()
            curr_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        res.append(curr_level)
        
    return res