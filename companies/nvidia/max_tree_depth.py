from base.treenode import TreeNode
from collections import deque

def maxTreeDepth(root: TreeNode | None) -> int:
    # 1. Create a helper function 
    def maxTreeDepthHelper(node: TreeNode | None) -> int:
        # 2. Check if the node is None. If so, return 0 because there are more
        # nodes in the tree to traverse
        if node is None:
            return 0
        
        # 3. Return the maximum depth of the left and right node and add one to traverse
        # further down the depth of the tree
        return max(maxTreeDepthHelper(node.left), maxTreeDepthHelper(node.right)) + 1

    # 4. Return the final result of the depth of the tree
    return maxTreeDepthHelper(root)

def maxTreeDepthBFS(root: TreeNode | None) -> int:
    # 1. Initialize the depth to be 1. The depth of a tree with a root node is 1
    depth = 1
    
    # 2. Create a queue to store all of the nodes
    queue = deque([root])
    
    while queue:
        # 3. Loop through every node in the queue
        for _ in range(len(queue)):
            # 4. Get the earliest node added to the queue
            node = queue.popleft()
            
            # 5. Add the node's children to the end of the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # 6. Add 1 to the tree's depth, signaling 
        # that one level down has been traversed through the tree
        depth += 1
    
    # 7. return the depth
    return depth