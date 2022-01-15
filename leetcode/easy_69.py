"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        return self.recursive_formula(x)
    
    def recursive_formula(self,d):
        x = 1
        res = 1e8
        previous = 1
        while res > 1/2:
            x = (previous + d/previous)/2
            res = abs(x - previous)
            previous = x
        x = int(round(x,1))
        if x**2 - d > 0:
            x-=1
        return x
        

if __name__ == '__main__':
    
    x = 4
    out = 2
    
    x = 8
    out = 2
    
    x = 2147395599
    out = 46339
    
    print(f'x: {x}')
    print(f'out: {out}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.mySqrt(x))
    
    
    print(f'time duration: {time() - start}')

"""
Runtime: 58 ms, faster than 35.75% of Python3 online submissions for Sqrt(x).
Memory Usage: 14.2 MB, less than 41.20% of Python3 online submissions for Sqrt(x).
"""