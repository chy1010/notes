"""
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

E.g.1:
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

E.g.2:
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        i = 0
        j = m-1
        while i < j:
            half = (i+j) // 2
            if matrix[half][0] <= target <= matrix[half][-1]:
                i = j = half
                break
            if target < matrix[half][0]:
                j = half-1
            elif target > matrix[half][-1]:
                i = half+1
        if j < i:
            return False
        # i == j
        if n == 1:
            return matrix[i][0] == target
        p = 0
        q = n-1
        while p < q:
            half = (p+q) // 2
            print(p, half, q)
            if matrix[i][half] == target:
                return True
            elif target > matrix[i][half]:
                p = half+1
            else: # target < matrix[i][half]:
                q = half-1
        if p == q:
            return matrix[i][p] == target
        return False
        
        

if __name__ == '__main__':
    
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    o = True
    
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    o = False
    
    matrix = [[3]]
    target = 3
    o = True
    
    matrix = [[1, 3]]
    target = 3
    o = True
    
    print(f'matrix: {matrix}; target: {target}')
    print(f'o: {o}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.searchMatrix(matrix, target))
    
    print(f'time duration: {time() - start}')
    

"""
Runtime: 44 ms, faster than 72.49% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 15 MB, less than 5.54% of Python3 online submissions for Search a 2D Matrix.
"""