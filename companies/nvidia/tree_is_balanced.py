from base.treenode import TreeNode

def treeIsBalanced(root: TreeNode):
    def treeIsBalancedHelper(node: TreeNode):
        if not node:
            return 0
        
        left = treeIsBalancedHelper(node.left)
        right = treeIsBalancedHelper(node.right)
        
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1
    
    return treeIsBalancedHelper(root) != -1
