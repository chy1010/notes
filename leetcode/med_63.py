"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.
"""
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1 or n == 1:
            if any(1 in row for row in obstacleGrid):
                return 0
            return 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                if i > 0:
                    obstacleGrid[i][j] += obstacleGrid[i-1][j]
                if j > 0:
                    obstacleGrid[i][j] += obstacleGrid[i][j-1]
        # for j in obstacleGrid:
        #     print(j)
        return obstacleGrid[-1][-1]
        

if __name__ == '__main__':
    
    obstacleGrid = [[0,1],[0,0]]
    expected = 1
    
    # obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    # expected = 2
    
    # obstacleGrid = [[0,1,0,0,0,0],[0,0,1,0,0,0]]
    # expected = 0
    
    # obstacleGrid = [[0]]
    # expected = 1
    
    # obstacleGrid = [[1]]
    # expected = 0
    
    # obstacleGrid = [[0,0,0,0,0]]
    # expected = 1
    
    # obstacleGrid = [[0,0],[0,0]]
    # expected = 2
    
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    expected = 2
    
    # obstacleGrid = [[0,0],[0,1]]
    # expected = 0

    import json
    with open('leetcode/test-data/med_63_data.json') as fp:
        obstacleGrid = json.load(fp)
    expected = None
    
    print(f'obstacleGrid')
    for obstacles in obstacleGrid:
        print(obstacles)
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.uniquePathsWithObstacles(obstacleGrid))
    # print(sol.uniquePaths(3,3))
    
    print(f'time duration: {time() - start}')
    
    
    
"""
Runtime: 84 ms, faster than 6.96% of Python3 online submissions for Unique Paths II.
Memory Usage: 14.5 MB, less than 35.19% of Python3 online submissions for Unique Paths II.
"""