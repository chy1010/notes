class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        left = None
        right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        if root == p or root == q: 
            return root
        if left and right: 
            return root
        if right: 
            return right
        if left: 
            return left
        return None