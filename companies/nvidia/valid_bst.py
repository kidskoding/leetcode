from base.treenode import TreeNode

def validBST(root: TreeNode | None):
    def validBSTHelper(node: TreeNode | None, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        
        return validBSTHelper(node.left, min_val, node.val) and \
            validBSTHelper(node.right, min_val, max_val)
    
    return validBSTHelper(root, float('-inf'), float('inf'))