from typing import Optional
from base.treenode import TreeNode

# Time: O(h) because you go down one path of the tree of height h
# Space: O(h) because the recursion call stack happens on a height h
def lca_bst(root: Optional[TreeNode], p, q):
    if p.val < root.val and q.val < root.val:
        return lca_bst(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lca_bst(root.right, p, q)
    
    return root