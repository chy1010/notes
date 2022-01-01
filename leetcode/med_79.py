"""
79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
from collections import defaultdict
from typing import List
from itertools import product

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not len(word):
            return True
        self.word_length = len(word)
        
        # {'a': coordinates of a, 'b': coordiantes of b, ...}
        coord_table = defaultdict(list)
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                coord_table[c].append((i,j))
        self.coord_table = coord_table
        
        is_exist, _ = self.sub_seq_exist(word = word)
        return is_exist
    
    def sub_seq_exist(self, word):
        """[summary]
        Args:
            word: check if word exists on the board

        Returns:
            is_exists: False if the word doesnot exist
            possible_chains: list of sequences of coordinates
                that corresponds all characters in the word.
                e.g. of the form [ [(a1, b1), (a2, b2), ...], [(c1, d1), (c2, d2), ...], ...]
                where (a1, b1) and (c1, d1) are coordinates of the first char in word, ... etc.
        """        
        if len(word) == 1:
            return (len(self.coord_table[word]) > 0), [ [coord] for coord in self.coord_table[word]]
        
        length = len(word)
        half = length // 2
        left = word[:half]
        right = word[half:]
        
        is_left_exists, left_chains = self.sub_seq_exist(left)
        is_right_exists, right_chains = self.sub_seq_exist(right)
            
        if not (is_left_exists and is_right_exists):
            return False, [[]]
        
        merged_chains = []
        for left_chain, right_chain in product(left_chains, right_chains):
            # check the continuity
            if self.check_neighbor(left_chain[-1], right_chain[0]):
                merged_chain = left_chain + right_chain
                
                # check if a position is passed twice.
                occupied_coords = set(merged_chain)
                if len(occupied_coords) < len(merged_chain):
                    continue
                
                # early return True if a successful case exists
                if len(occupied_coords) == self.word_length:
                    return True, [[]]
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
    
    board = [['a']]
    word = 'ab'
    
    board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
    word = "AAAAAAAAAAAAABB"
    
    # board = [["B","B","B","B"],["B","B","B","B"],["B","C","B","B"],["B","B","B","B"],["B","B","B","B"]]
    # word = "BBBBBBBBBBBBBCB"
    
    # board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
    # word = "BBAAAAAAAAAAAAA"
    
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # word = "ABCCED"
    
    # board = [["a"]]
    # word = "b"
    
    for row in board:
        for c in row:
            print(c, end=' ')
        print('')
    print(f'word = {word}')
    print('-'*30)
    sol = Solution()
    from time import time
    start_time = time()
    print(sol.exist(board=board, word=word))
    print(f'duration time: {time() - start_time}')