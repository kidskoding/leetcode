from tree_node import TreeNode
from typing import Optional

def height(node: Optional[TreeNode]) -> int:
    if node is None:
        return 0
    
    return max(height(node.left), height(node.right)) + 1