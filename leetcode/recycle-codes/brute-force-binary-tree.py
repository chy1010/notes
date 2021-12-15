
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

    def __repr__(self):
        msg = ''
        this_level = [self.root]
        while len(this_level) > 0:
            for node in this_level:
                if node is None:
                    msg += 'x, '
                else:
                    msg += str(node) + ', '
            next_level = [node for leaf in this_level if leaf is not None for node in (leaf.left, leaf.right) if node is not None]
            this_level = next_level
            msg+='\n'
        return msg
                


if __name__ == '__main__':
    print('Generating a binary tree:')

    from time import time
    start_time = time()
    T = BinaryTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(f'time duration: {time() - start_time}')
    print(T)