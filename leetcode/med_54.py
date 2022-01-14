"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = n-1
        k = 0
        l = m-1
        outputs = []
        while (i <= j) and (k <= l):
            if i == j:
                this_layer = matrix[i][k:l+1]
            elif k == l:
                this_layer = [matrix[p][k] for p in range(i,j+1)]
            else:
                this_layer = [
                    *matrix[i][k:l+1],
                    *[ matrix[p][l] for p in range(i+1,j)],
                    *matrix[j][l:k:-1],
                    *[ matrix[p][k] for p in range(j,i,-1)],
                    ]
            outputs.extend(this_layer)
            i+=1
            j-=1
            k+=1
            l-=1
        return outputs

if __name__ == '__main__':
    
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    expected = [1,2,3,6,9,8,7,4,5]
    
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    expected = [1,2,3,4,8,12,11,10,9,5,6,7]
    
    print(f'matrix: {matrix}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.spiralOrder(matrix))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 28 ms, faster than 87.53% of Python3 online submissions for Spiral Matrix.
Memory Usage: 14.3 MB, less than 58.65% of Python3 online submissions for Spiral Matrix.
"""