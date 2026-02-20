from base.treenode import TreeNode
from collections import deque

def rightSideView(root: TreeNode):
    # 1. If there is no root node, return an empty list of the right side node
    if not root:
        return []
    
    # 2. Create a queue that stores all the tree nodes by level
    queue = deque([root])
    
    # 3. Create a list that gets all the right most nodes of the tree
    rightMostNodes = []
    
    while queue:
        # 4. Get the size of the current queue
        level_size = len(queue)
        for i in range(level_size):
            # 5. Get the left most node of the queue
            node = queue.popleft()
            
            # 6. If at the last node in the level, add it to the right most nodes
            if i == level_size - 1:
                rightMostNodes.append(node.val)
            
            # 7. Add children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    # 8. Return the right most nodes
    return rightMostNodes