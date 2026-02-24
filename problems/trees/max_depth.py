from typing import Optional
from problems.trees.tree_node import TreeNode

def maxDepth(root: Optional[TreeNode]):
    if root is None:
        return 0
    
    return max(maxDepth(root.left), maxDepth(root.right)) + 1