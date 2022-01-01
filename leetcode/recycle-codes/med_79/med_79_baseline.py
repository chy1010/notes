"""
79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
from collections import defaultdict
from typing import List
from copy import deepcopy

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(next(iter(board)))
        
        counts = defaultdict(int)
        for c in word:
            counts[c]+=1
            
        coord_table = defaultdict(list)
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                coord_table[c].append((i,j))
        # coord_table = dict(coord_table)
        # print(counts)
        # for c in coord_table:
        #     print(f'{c}: {len(coord_table[c])}')
                
        if not all([ repeats <= len(coord_table[c]) for c, repeats in counts.items()]):
            return False
        
        return self.chess_move(remain_chars=word, chars_coord_table=coord_table)
        
    def chess_move(self, remain_chars, chars_coord_table, cursor = None):
        """[summary]
        Args:
            remain_chars (str): remaining characters need to find on the table
            chars_coord_table (dict): positions of the remain characters
            cursor (tuple):
                The position of the last found char.
                If None, now is finding the first char.
        Returns:
            If the first remaining char is found and is the neighbor of the previous char.
            Then check the next step.
        """
        c = remain_chars[0]
        # print(f'Finding {c}.')
        # print(f'next_move: {chars_coord_table[c]}')
        for next_move in chars_coord_table[c]:
            # if cursor is None: this is the first char to find.
            if self.check_neighbor(cursor, next_move):
                if len(remain_chars) == 1:
                    return True
                next_coord_table = deepcopy(chars_coord_table)
                next_coord_table[c].remove(next_move)
                
                if self.chess_move(remain_chars=remain_chars[1:], chars_coord_table=next_coord_table, cursor=next_move):
                    return True
        return False            
                    
                
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
    
    # print(f'board = {board}')
    for row in board:
        for c in row:
            print(c, end=' ')
        print('')
    print(f'word  = {word}')
    sol = Solution()
    print(sol.exist(board=board, word=word))