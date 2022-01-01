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
        self.p = p.val
        self.q = q.val

        good_root = self.clean_structure(root)
        # early stop if p is an ancestor of q or vice versa.
        if isinstance(good_root, tuple):
            ret = p if p.val == good_root[0] else q
            return ret
        root = good_root

        path_to_p = []
        while p.val != root.val:
            path_to_p.append(p.val)
            p = self.ancestor_of_p(root, p)
        path_to_p.append(root.val)

        while q.val not in path_to_p:
            q = self.ancestor_of_p(root, q)
        return q

    def clean_structure(self, root: TreeNode):
        # `good` means
        # (i) Both of the left and right descendants of a node are not None.
        # (ii) Both of the left and right descendants of a node are None.

        good_root = self.return_good_node(root)
        # early stop
        if isinstance(good_root, tuple):
            return good_root
        root = good_root
        stems = [root]
        while len(stems) > 0:
            # for each good node, make its left and right descendants also good:
            stem = stems.pop(0)
            if stem.left is not None:
                # this stem is a good node.
                assert stem.right is not None
                good_node = self.return_good_node(stem.left)
                # early return
                if isinstance(good_node, tuple):
                    return good_node
                stem.left = good_node

                good_node = self.return_good_node(stem.right)
                # early return
                if isinstance(good_node, tuple):
                    return good_node
                stem.right = good_node

                stems.append(stem.left)
                stems.append(stem.right)
        return root

    def return_good_node(self, leaf):
        # ``only two descendants are both None or not None.`` is good.
        # if this node is not good, just merge a good descendant to this node.
        while (leaf.left is None) ^ (leaf.right is None):
            val = leaf.val  # keep the value if it is p or q
            if leaf.left is not None:
                leaf = leaf.left
            else:
                leaf = leaf.right

            # if p or q is an ancestor of q or p, then just early return
            # before to merge them.
            # return tuple to make differences with normal return
            if val == self.p and leaf.val == self.q:
                return (val, 'p is an ancestor of q')
            elif val == self.q and leaf.val == self.p:
                return (val, 'q is an ancestor of p')

            if val == self.p or val == self.q:
                leaf.val = val
        return leaf

    @staticmethod
    def ancestor_of_p(root: TreeNode, p: TreeNode):
        # brute force
        this_level = [root]
        while len(this_level) > 0:
            for node in this_level:
                if (node.left is not None and node.left.val == p.val) or (
                        node.right is not None and node.right.val == p.val):
                    return node
            next_level = [
                node for leaf in this_level if leaf is not None
                for node in (leaf.left, leaf.right) if node is not None
            ]
            this_level = next_level
        raise 'No ancestor'