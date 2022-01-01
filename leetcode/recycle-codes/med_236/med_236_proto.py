"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
from typing import List, Union, Optional

# Definition for a binary tree node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class Solution:
    def lowestCommonAncestor(self, root: List[int], p: TreeNode, q: TreeNode) -> TreeNode:
        T = BinaryTree(root)
        path_1 = [str(node) for node in T.path_to_p(p)]
        path_2 = [node for node in T.path_to_p(q) if str(node) in path_1]
        return path_2[-1]


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
            next_level = [node for leaf in this_level if leaf is not None for node in (leaf.left, leaf.right)]
            for node in this_level:
                if node is None:
                    continue
                if (isinstance(node.left, TreeNode) and node.left.val == p.val) or (
                    isinstance(node.right, TreeNode) and node.right.val == p.val):
                    return node

            if all([node is None for node in next_level]):
                return None
            this_level = next_level


    def __repr__(self):
        msg = ''
        this_level = [self.root]
        while len(this_level) > 0:
            next_level = [node for leaf in this_level if leaf is not None for node in (leaf.left, leaf.right)]
            for node in this_level:
                if node is None:
                    msg += 'x, '
                else:
                    msg += str(node) + ', '
            if all([node is None for node in next_level]):
                break
            msg+='\n'
            this_level = next_level
        return msg
                


if __name__ == '__main__':
    # print('generating binary tree:')
    # T = BinaryTree([3,5,1,6,2,0,8,None,None,7,4])
    
    # the_path = T.path_to_p(7)
    # for node in the_path:
    #     print(node.val)

    sol = Solution()
    sol.lowestCommonAncestor(root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4)