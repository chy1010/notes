"""
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

E.g.1:
Input: x = 2.00000, n = 10
Output: 1024.00000

E.g.2:
Input: x = 2.10000, n = 3
Output: 9.26100

E.g.3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.pow(1/x, -n)
        return self.pow(x, n)

    def pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 0:
            return self.pow(x**2, n//2)
        return x * self.pow(x**2, n//2)

if __name__ == '__main__':
    
    x = 2.00000
    n = 10
    expected = 1024.00000
    
    x = 2.10000
    n = 3
    expected = 9.26100
    
    x = 2.00000
    n = -2
    expected = 0.25000
    
    x = 0.00001
    n = 2147483647
    expected = ''

    
    print(f'x: {x}; n: {n}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.myPow(x, n))
    
    print(f'time duration: {time() - start}')


"""
Runtime: 63 ms, faster than 5.02% of Python3 online submissions for Pow(x, n).
Memory Usage: 14.3 MB, less than 18.32% of Python3 online submissions for Pow(x, n).
"""