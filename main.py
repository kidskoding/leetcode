from base.treenode import TreeNode
from problems.trees.is_balanced import isBalanced

root = TreeNode(
    1,
    TreeNode(
        2,
        None,
        None
    ),
    TreeNode(
        TreeNode(4, TreeNode(5), None),
        None,
        None
    )
)

print(isBalanced(root))