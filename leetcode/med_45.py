"""
Given an array of non-negative integers nums,
you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

E.g.1.
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

E.g.2.
Input: nums = [2,3,0,1,4]
Output: 2
"""
from typing import List
import numpy as np

class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        last_index = len(nums) - 1
        jumps = 0
        location = 0
        while True:
            remain_steps = nums[location]
            if location + remain_steps >= last_index:
                return jumps + 1
            possible_choices = nums[location+1: location+remain_steps+1]
            dist_expectation = np.asarray(list(map(lambda x,y: x+y, possible_choices, range(-(last_index-location-1),1))))
            optimized_steps = np.max(dist_expectation)
            
            # np.where returns tuple, get farest position
            dist_to_maximize_steps = np.where(dist_expectation==optimized_steps)[0][-1].item() + 1
            jumps += 1
            location += dist_to_maximize_steps
            # if location >= last_index:
            #     return jumps

if __name__ == '__main__':
    
    nums = [2,3,1,1,4]
    expected = 2
    
    nums = [2,3,0,1,4]
    expected = 2
    
    nums = [1,2,3,4,3,2,3,4,1,1,1,2,3,1,1,1]
    expected = 6
    
    nums = [1,2,3]
    expected = 2
    
    nums = [4,1,1,3,1,1,1]
    expected = 2
    
    nums = [3,4,3,2,5,4,3]
    expected = 3
    
    nums = [3,2,1]
    expected = 1
    
    nums = [1,2,1,1,1]
    expected = 3
    
    # nums = [10,9,8,7,6,5,4,3,2,1,1,0]
    # expected = 2
    
    print(f'nums: {nums}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.jump(nums))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 600 ms, faster than 36.96% of Python3 online submissions for Jump Game II.
Memory Usage: 31.7 MB, less than 5.00% of Python3 online submissions for Jump Game II.
Runtime: 487 ms, faster than 39.09% of Python3 online submissions for Jump Game II.
Memory Usage: 32.1 MB, less than 5.00% of Python3 online submissions for Jump Game II.
"""
