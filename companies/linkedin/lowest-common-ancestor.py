def lowestCommonAncestor(root, p, q):
    # base case:
    # if we reach the end of a path, return None
    # if we find p or q, return that node
    if not root or root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    # if both sides returned a node, then p and q were found
    # in different subtrees, so current root is the LCA
    if left and right:
        return root
    
    # otherwise return whichever side found something
    return left if left else right