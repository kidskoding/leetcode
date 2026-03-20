from typing import Optional
from base.treenode import TreeNode

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))