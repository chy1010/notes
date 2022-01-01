"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
from typing import List, Union, Optional
import json

# Definition for a binary tree node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def __str__(self):
    #     return str(self.val)


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode,
                             q: TreeNode) -> TreeNode:
        if isinstance(p, int): p = TreeNode(p)
        if isinstance(q, int): q = TreeNode(q)
        self.p = p.val
        self.q = q.val

        good_root = self.clean_structure(root)
        if isinstance(good_root, tuple):
            ret = p if p.val == good_root[0] else q
            return ret
        root = good_root

        path_p = []
        while p.val != root.val:
            path_p.append(p.val)
            p = self.ancestor_of_p(root, p)
        path_p.append(root.val)

        while q.val not in path_p:
            q = self.ancestor_of_p(root, q)
        return q

    def clean_structure(self, root: TreeNode):
        good_leaf = self.return_good_leaf(root)
        if isinstance(good_leaf, tuple):
            return good_leaf
        root = good_leaf
        stems = [root]
        while len(stems) > 0:
            stem = stems.pop(0)
            if stem.left is not None:
                assert stem.right is not None
                good_leaf = self.return_good_leaf(stem.left)
                if isinstance(good_leaf, tuple):
                    return good_leaf
                stem.left = good_leaf
                good_leaf = self.return_good_leaf(stem.right)
                if isinstance(good_leaf, tuple):
                    return good_leaf
                stem.right = good_leaf
                stems.append(stem.left)
                stems.append(stem.right)
        return root

    def return_good_leaf(self, leaf):
        while (leaf.left is None) ^ (leaf.right is None):
            val = leaf.val
            if leaf.left is not None:
                leaf = leaf.left
            else:
                leaf = leaf.right
            if val == self.p and leaf.val == self.q:
                return (val, 'p is an ancestor of q')
            elif val == self.q and leaf.val == self.p:
                return (val, 'q is an ancestor of p')
            if val == self.p or val == self.q:
                leaf.val = val
        return leaf

    @staticmethod
    def ancestor_of_p(root: TreeNode, p: TreeNode):
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

    @staticmethod
    def show_tree(p: TreeNode):
        msg = ''
        this_level = [p]
        while len(this_level) > 0:
            next_level = [
                node for leaf in this_level if leaf is not None
                for node in (leaf.left, leaf.right)
            ]
            for node in this_level:
                if node is None:
                    msg += 'x, '
                else:
                    msg += str(node.val) + ', '
            if all([node is None for node in next_level]):
                break
            msg += '\n'
            this_level = next_level
        print(msg)


class BinaryTree:
    def __init__(self, root: List[int]):

        self.root = TreeNode(root.pop(0))
        self.leaves = [self.root]

        while len(root) > 0:
            # print(f'rest number of nodes: {len(root)}')
            level_num_leaves = 2 * len(self.leaves)
            new_leaf_values = root[:level_num_leaves]
            new_leaves = list()
            for leaf in self.leaves:
                if len(new_leaf_values) == 0:
                    new_leaves.append(leaf)
                    continue
                val = new_leaf_values.pop(0)
                if val is not None:
                    leaf.left = TreeNode(val)
                    new_leaves.append(leaf.left)
                    # print(f'{val} is added on the left of {leaf}')

                if len(new_leaf_values) == 0:
                    continue
                val = new_leaf_values.pop(0)
                if val is not None:
                    leaf.right = TreeNode(val)
                    new_leaves.append(leaf.right)
                    # print(f'{val} is added on the right of {leaf}')
            self.leaves = new_leaves
            root = root[level_num_leaves:]

    def path_to_p(self, p: Optional[Union[TreeNode, int]]):
        if p is None:
            return []
        if isinstance(p, int):
            p = TreeNode(p)
        if p.val == self.root.val:
            return [self.root]
        else:
            source = self.source_of_p(p)
            return [*self.path_to_p(source), p]

    def source_of_p(self, p: TreeNode):
        this_level = [self.root]
        while len(this_level) > 0:
            next_level = [
                node for leaf in this_level if leaf is not None
                for node in (leaf.left, leaf.right)
            ]
            for node in this_level:
                if node is None:
                    continue
                if (isinstance(node.left, TreeNode)
                        and node.left.val == p.val) or (isinstance(
                            node.right, TreeNode) and node.right.val == p.val):
                    return node

            if all([node is None for node in next_level]):
                return None
            this_level = next_level

    def __repr__(self):
        msg = ''
        this_level = [self.root]
        while len(this_level) > 0:
            next_level = [
                node for leaf in this_level if leaf is not None
                for node in (leaf.left, leaf.right)
            ]
            for node in this_level:
                if node is None:
                    msg += 'x, '
                else:
                    msg += str(node.val) + ', '
            if all([node is None for node in next_level]):
                break
            msg += '\n'
            this_level = next_level
        return msg


if __name__ == '__main__':

    # T = BinaryTree([3,None,5,1,None,2,4])
    # print(T)
    # print('-=-'*30)
    # sol = Solution()
    # LCA = sol.lowestCommonAncestor(root=T.root, p = 5, q = 2)
    # raise 'Stop'

    with open('leetcode/recycle-codes/med_236/test_data.txt') as fp:
        data = fp.read().splitlines()
    root = data[0].lstrip('[').rstrip(']').split(',')
    root = [json.loads(item) for item in root]
    p = json.loads(data[1])
    q = json.loads(data[2])
    print('generating binary tree:')

    from time import time
    start_time = time()
    T = BinaryTree(root)
    print(f'time duration for generating the binary tree: {time()-start_time}')

    # for leaf in T.leaves:
    #     print(leaf.val, end=', ')
    # raise 'Stop'
    # T = BinaryTree([3,5,1,6,2,0,8,None,None,7,4])

    # the_path = T.path_to_p(7)
    # for node in the_path:
    #     print(node.val)
    # print(T)

    start_time = time()
    sol = Solution()
    LCA = sol.lowestCommonAncestor(root=T.root, p=p, q=q)
    print(f'time duration for solving this: {time()-start_time}')
    print(LCA.val)
