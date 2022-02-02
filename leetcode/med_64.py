"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

E.g.1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

E.g.2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1:
            return sum(grid[0])
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                elif i > 0:
                    grid[i][j] += grid[i-1][j]
                elif j > 0:
                    grid[i][j] += grid[i][j-1]
        return grid[-1][-1]
                    
        

if __name__ == '__main__':
    
    
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    expected = 7
    
    grid = [[1,2,3],[4,5,6]]
    expected = 12
    
    print(f'grid: {grid}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.minPathSum(grid))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 90 ms, faster than 94.01% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15.5 MB, less than 88.55% of Python3 online submissions for Minimum Path Sum.
"""