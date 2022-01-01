"""
79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
from collections import defaultdict
from typing import List, Tuple, Union
from itertools import product

class Wordpath:
    def __init__(self,
                 head: Tuple[int, int],
                 tail: Tuple[int, int],
                 components: Union[List, set]):
        self.head = head
        self.tail = tail
        self.components = set(components)
        
    def __len__(self):
        return len(self.components)
        
    def __eq__(self, another_path):
        return (self.head == another_path.head) and (
            self.tail == another_path.tail) and (
            self.components == another_path.components)
            
    def __add__(self, another_path):
        return Wordpath(self.head, another_path.tail, self.components.union(another_path.components))

    @staticmethod
    def check_neighbor(coord_1, coord_2):
        if coord_1 is None or coord_2 is None:
            return True
        a, b = coord_1
        c, d = coord_2
        return (a==c and (b==d+1 or d==b+1)) or (b==d and (a==c+1 or c==a+1))
    
    def mergable(self, another_path):
        return self.check_neighbor(self.tail, another_path.head)

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
            return (len(self.coord_table[word]) > 0), [ Wordpath(coord, coord, [coord]) for coord in self.coord_table[word]]
        
        length = len(word)
        half = length // 2
        left = word[:half]
        right = word[half:]
        
        is_left_exists, left_word_paths = self.sub_seq_exist(left)
        is_right_exists, right_word_paths = self.sub_seq_exist(right)
            
        if not (is_left_exists and is_right_exists):
            return False, [[]]
        
        merged_chains = []
        for left_word, right_word in product(left_word_paths, right_word_paths):
            # check the continuity
            if left_word.mergable(right_word):
                merged_word = left_word + right_word
                
                # check if a position is passed twice.
                if len(merged_word) < len(left_word) + len(right_word):
                    continue
                
                # early return True if a successful case exists
                if len(merged_word) == self.word_length:
                    return True, [[]]
                if merged_word not in merged_chains:
                    merged_chains.append(merged_word)
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
    
    board = [["B","B","B","B"],["B","B","B","B"],["B","C","B","B"],["B","B","B","B"],["B","B","B","B"]]
    word = "BBBBBBBBBBBBBCB"
    
    # board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
    # word = "BBAAAAAAAAAAAAA"
    
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # word = "ABCCED"
    
    # board = [["a"]]
    # word = "b"
    
    # path1 = Wordpath((0,0), (1,1), [(0,0), (0,1), (0,2), (1,2), (2,2), (2,1), (2,0), (1,0), (1,1)])
    # path2 = Wordpath((0,0), (1,1), [(0,0), (1,0), (2,0), (2,1), (2,2), (1,2), (0,2), (0,1), (1,1)])
    
    # path_list = [path1]
    # print(path1 in path_list)
    
    # path3 = Wordpath((0,0), (2,3), [(0,0), (0,1), (0,2), (1,2), (2,2), (2,3)])
    # path4 = Wordpath((2,4), (4,5), [(2,4), (3,4), (4,4), (4,5)])
    
    # path5 = path3 + path4
    # print(path5.head)
    # print(path5.tail)
    # print(path5.components)
    # print(path1 == path2)
    # raise 'Stop'
    
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