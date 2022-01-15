"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

E.g.1
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

E.g.2
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
from functools import reduce
class Solution:
    def climbStairs(self, n: int) -> int:
        max_2_steps = n // 2
        remain_1_steps = n % 2
        return sum([ self.combinations(i + (max_2_steps-i)*2 + remain_1_steps, (max_2_steps-i)*2 + remain_1_steps) for i in range(max_2_steps,-1,-1)])
    
    @staticmethod
    def combinations(m, n):
        n = min(n, m-n)
        if n == 0:
            return 1
        if n == 1:
            return m
        return int(reduce(lambda a,b: a*b, range(m,m-n,-1)) / reduce(lambda a,b: a*b, range(1,n+1)))
    
if __name__ == '__main__':
    
    
    n = 3
    o = 2
    
    print(f'n: {n}')
    print(f'o: {o}')
    
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.climbStairs(n))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 45 ms, faster than 20.47% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.5 MB, less than 11.63% of Python3 online submissions for Climbing Stairs.
"""