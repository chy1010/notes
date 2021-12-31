"""
79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
from collections import defaultdict
from typing import List
from copy import deepcopy
from itertools import product
import numpy as np

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(next(iter(board)))
        self.table = np.zeros(shape=(m, n))
            
        coord_table = defaultdict(list)
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                coord_table[c].append((i,j))        
        self.coord_table = coord_table
        
        is_exist, merged_chains = self.check_exist(word = word)
        if not is_exist:
            return False
        
        for possible_coords in merged_chains:
            table = deepcopy(self.table)
            fail = False
            for coord in possible_coords:
                if coord is None:
                    continue
                if table[coord] > 0:
                    fail = True
                    break
                table[coord] += 1
            if not fail:
                return True
        return False
    
    def check_exist(self, word):    
        if len(word) == 0:
            return True, [[None]]
        elif len(word) == 1:
            return True, [ [coord] for coord in self.coord_table[word]]
        
        length = len(word)
        half = length // 2
        left = word[:half]
        right = word[half:]
        
        is_left_exists, left_chains = self.check_exist(left)
        is_right_exists, right_chains = self.check_exist(right)
            
        if not (is_left_exists and is_right_exists):
            return False, [[]]
        
        merged_chains = []
        for left_chain, right_chain in product(left_chains, right_chains):
            if self.check_neighbor(left_chain[-1], right_chain[0]):
                table = deepcopy(self.table)
                fail = False
                for coord in left_chain:
                    if coord is None:
                        continue
                    if table[coord] > 0:
                        fail = True
                        break
                    table[coord] += 1
                if fail:
                    continue
                for coord in right_chain:
                    if table[coord] > 0:
                        fail = True
                        break
                    table[coord] += 1
                if fail:
                    continue
                merged_chain = right_chain if left_chain[0] is None else left_chain + right_chain
                merged_chains.append(merged_chain)
        return (len(merged_chains) > 0), merged_chains

    @staticmethod
    def check_neighbor(coord_1, coord_2):
        if coord_1 is None or coord_2 is None:
            return True
        a, b = coord_1
        c, d = coord_2
        return (a==c and (b==d+1 or d==b+1)) or (b==d and (a==c+1 or c==a+1))
        


if __name__ == '__main__':
    
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = 'ABCC'
    
    # board = [['a']]
    # word = 'ab'
    
    # board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
    # word = "AAAAAAAAAAAAABB"
    
    board = [["B","B","B","B"],["B","B","B","B"],["B","C","B","B"],["B","B","B","B"],["B","B","B","B"]]
    word = "BBBBBBBBBBBBBCB"
    
    # board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
    # word = "BBAAAAAAAAAAAAA"
    
    # print(f'board = {board}')
    for row in board:
        for c in row:
            print(c, end=' ')
        print('')
    print(f'word = {word}')
    print('-=-'*30)
    sol = Solution()
    from time import time
    start_time = time()
    print(sol.exist(board=board, word=word))
    print(f'duration time: {time() - start_time}')