"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.

E.g.1:
matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

E.g.2:
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
from typing import List
from functools import reduce
from itertools import product
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeros = []
        for i, j in product(range(m), range(n)):
            if matrix[i][j] == 0:
                zeros.append((i,j))
        for i, j in zeros:
            matrix[i][:] = [0]*n
            for p in range(m):
                matrix[p][j] = 0
        
        
    
if __name__ == '__main__':
    
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    o = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    
    for row in matrix:
        print(row)
    print('expected:')
    for row in o:
        print(row)
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    sol.setZeroes(matrix)
    for row in matrix:
        print(row)
    
    print(f'time duration: {time() - start}')

"""
Runtime: 124 ms, faster than 92.23% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 15.2 MB, less than 46.78% of Python3 online submissions for Set Matrix Zeroes.
"""