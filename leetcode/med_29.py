"""
Given two integers dividend and divisor,
divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero,
which means losing its fractional part.
For example, 8.345 would be truncated to 8,
and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within
the 32-bit signed integer range: [-2^31, 2^31-1].
For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1,
and if the quotient is strictly less than -2^31, then return -2^31.

E.g.1
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

E.g.2
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if not dividend:
            return 0
        # overflow case:
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        sign = -1 if ((dividend > 0) ^ (divisor > 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:    
            return self.format_result(dividend, sign)
            
        multipler = 0
        while divisor <= dividend:
            d = divisor
            i = 0
            while (d<<1) <= dividend:
                d = d<<1
                i += 1
            dividend -= d
            multipler += ((2<<(i-1)) if i > 0 else 1)
        return self.format_result(multipler, sign)
            
    def format_result(self, num, sign):
        assert num >= 0
        bm = str(bin(num))[2:]
        if sign < 0:
            if len(bm) > 32 or bm == '1' + ''.join(['0']*31):
                return -2**31
            return -num
        else:
            if len(bm) > 31:
                return 2**31-1
            return num
            
    
            

if __name__ == '__main__':
    
    
    dividend = 10
    divisor = 3
    expected = 3
    
    # dividend = 7
    # divisor = -3
    # expected = -2
    
    dividend = 1
    divisor = 1
    expected = 1
    
    dividend = 1
    divisor = 2
    expected = dividend // divisor
    
    dividend = 2147483647
    divisor = 2
    expected = dividend // divisor
    
    print(f'dividend: {dividend}')
    print(f'divisor: {divisor}')
    print(f'expected: {expected}')
    
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.divide(dividend=dividend, divisor=divisor))
    
    print(f'time duration: {time() - start}')
    
    
"""
Runtime: 41 ms, faster than 23.55% of Python3 online submissions for Divide Two Integers.
Memory Usage: 14.2 MB, less than 81.80% of Python3 online submissions for Divide Two Integers.
"""