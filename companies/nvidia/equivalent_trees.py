from base.treenode import TreeNode

def equivalentTrees(p: TreeNode, q: TreeNode):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    
    return equivalentTrees(p.left, q.left) and \
           equivalentTrees(p.right, q.right)