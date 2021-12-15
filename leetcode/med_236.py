"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode,
                             q: TreeNode) -> TreeNode:
        path_p = [node.val for node in self.path_to_p(root, p)]
        while q.val not in path_p:
            q = self.ancestor_of_p(root, q)
        return q

    def path_to_p(self, root: TreeNode, p: TreeNode):
        if p.val == root.val:
            return [root]
        else:
            ancestor = self.ancestor_of_p(root, p)
            return [*self.path_to_p(root, ancestor), p]

    @staticmethod
    def ancestor_of_p(root: TreeNode, p: TreeNode):
        search_level = [root]
        while len(search_level) > 0:
            for node in search_level:
                if (node.left is not None and node.left.val == p.val) or (
                        node.right is not None and node.right.val == p.val):
                    return node
            next_level = [
                node for leaf in search_level if leaf is not None
                for node in (leaf.left, leaf.right) if node is not None
            ]
            search_level = next_level
        raise 'No ancestor'
