"""
You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.
"""
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        i, j = 0, size - 1
        while i < j:
            temp = matrix[i][i:j+1]
            matrix[i][i:j+1] = [ matrix[k][i] for k in range(j, i-1, -1) ]
            for k in range(i,j+1):
                matrix[k][i] = matrix[j][k]
            matrix[j][i:j+1] = [ matrix[k][j] for k in range(j, i-1, -1) ]
            for k in range(i,j+1):
                matrix[k][j] = temp[k-i]
            del temp
            i+=1
            j-=1

if __name__ == '__main__':
    
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # expected = [[7,4,1],[8,5,2],[9,6,3]]
    
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    
    print(f'matrix: {matrix}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    sol.rotate(matrix)
    print(matrix)
    
    print(f'time duration: {time() - start}')

"""
Runtime: 84 ms, faster than 5.41% of Python3 online submissions for Rotate Image.
Memory Usage: 14.3 MB, less than 30.72% of Python3 online submissions for Rotate Image.
"""