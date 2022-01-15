"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.
"""
from functools import reduce
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        m=m-1
        n=n-1
        return int(reduce(lambda a,b: a*b, range(m+n, max(m,n), -1)) / reduce(lambda a,b:a*b, range(1,min(m,n)+1)))

if __name__ == '__main__':
    
    m = 3
    n = 7
    expected = 28
    
    print(f'm: {m}; n: {n}')
    print(f'expected: {expected}')
    
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.uniquePaths(m, n))
    
    
    print(f'time duration: {time() - start}')

"""
Runtime: 28 ms, faster than 87.96% of Python3 online submissions for Unique Paths.
Memory Usage: 14.1 MB, less than 96.26% of Python3 online submissions for Unique Paths.
"""