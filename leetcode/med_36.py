"""
Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:
    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        patches = defaultdict(set)
        for i, row in enumerate(board):
            this_row = set()
            for j, num in enumerate(row):
                if num == '.':
                    continue
                if num in this_row.union(columns[j]).union(patches[(i//3, j//3)]):
                    return False
                this_row.add(num)
                patches[(i//3, j//3)].add(num)
                columns[j].add(num)
        return True

if __name__ == '__main__':
    
    board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
    
    expected = True
    
    # board = [["8","3",".",".","7",".",".",".","."],
    #     ["6",".",".","1","9","5",".",".","."],
    #     [".","9","8",".",".",".",".","6","."],
    #     ["8",".",".",".","6",".",".",".","3"],
    #     ["4",".",".","8",".","3",".",".","1"],
    #     ["7",".",".",".","2",".",".",".","6"],
    #     [".","6",".",".",".",".","2","8","."],
    #     [".",".",".","4","1","9",".",".","5"],
    #     [".",".",".",".","8",".",".","7","9"]]
    
    # expected = False
    
    # board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # expected = True
    
    from pprint import pprint
    pprint(board)
    print(f'expected: {expected}')
    
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.isValidSudoku(board))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 175 ms, faster than 9.37% of Python3 online submissions for Valid Sudoku.
Memory Usage: 14.2 MB, less than 89.81% of Python3 online submissions for Valid Sudoku.
"""