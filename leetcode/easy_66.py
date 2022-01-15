"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.insert(0,0)
        carry = 1
        for j in range(len(digits)-1, -1, -1):
            digits[j] += carry
            carry = digits[j] // 10
            digits[j] = digits[j] % 10
        if digits[0] == 0:
            return digits[1:]
        return digits

if __name__ == '__main__':
    
    digits = [4,3,2,1]
    expected = [4,3,2,2]
    
    print(f'digits: {digits}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.plusOne(digits))
    
    print(f'time duration: {time() - start}')


"""
Runtime: 53 ms, faster than 15.07% of Python3 online submissions for Plus One.
Memory Usage: 14.2 MB, less than 75.76% of Python3 online submissions for Plus One.
"""