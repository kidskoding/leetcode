from typing import Optional
from base.treenode import TreeNode

# Time O(n) — visit every node once
# Space O(h) — call stack depth equals tree height
def validBST(root: Optional[TreeNode]):
    def validate(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
    
    return validate(root, float('-inf'), float('inf'))