from base.treenode import TreeNode
from companies.nvidia.right_side_view import rightSideView

root = TreeNode(
    1,
    TreeNode(
        2,
        None,
        TreeNode(5)
    ),
    TreeNode(
        3,
        None,
        TreeNode(4)
    )
)
print(rightSideView(root))