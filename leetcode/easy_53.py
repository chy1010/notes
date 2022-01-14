"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

E.g.1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

E.g.2:
Input: nums = [1]
Output: 1

E.g.3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        now_record = None
        now_sum = 0
        for num in nums:
            if now_sum < 0 and num > 0:
                now_sum = num
            elif now_sum + num > 0:
                now_sum += num
            else:
                now_sum = num
            if now_record is None or now_sum > now_record:
                now_record = now_sum
                
        return now_record
        

if __name__ == '__main__':
    
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    expected = 6
    
    nums = [1]
    expected = 1
    
    nums = [5,4,-1,7,8]
    expected = 23
    
    print(f'nums: {nums}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.maxSubArray(nums))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 724 ms, faster than 80.64% of Python3 online submissions for Maximum Subarray.
Memory Usage: 28 MB, less than 95.69% of Python3 online submissions for Maximum Subarray.
"""