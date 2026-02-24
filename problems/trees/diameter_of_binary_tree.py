from problems.trees.tree_node import TreeNode
from typing import Optional

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter = 0

    def height(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)
        diameter = max(diameter, left_height + right_height)

        return max(left_height, right_height) + 1

    height(root)
    return diameter