from problems.trees.tree_node import TreeNode

def invertBinaryTree(root: TreeNode):
    if root is None:
        return None

    root.left, root.right = root.right, root.left
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    
    return root