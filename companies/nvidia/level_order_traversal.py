from base.treenode import TreeNode
from collections import deque

def levelOrderTraversal(root: TreeNode):
    if not root:
        return []
    
    # 1. Create a queue to store the nodes
    queue = deque([root])
    
    # 2. Create a list to store a list of nodes at each level
    nodes = []
    
    # 3. While there are nodes in the queue
    while queue:
        # 4. Create a list to store the nodes at the current level
        nodesInLevel = []
        
        # Go through all the nodes in the queue
        for _ in range(len(queue)):
            # 5. Get the earliest node in the queue (because it comes the earliest in the tree)
            node = queue.popleft()
            
            # 6. Add its value to the list of nodes in the current level
            nodesInLevel.append(node.val)
            
            # 7. Add child nodes to the queue depending on which child nodes are available
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # 8. Add all the nodes in level to nodes
        nodes.append(nodesInLevel)
    
    # 9. Return all the nodes
    return nodes