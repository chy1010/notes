"""
You are given an integer array nums.
You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

E.g.1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

E.g.2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""
from typing import List
import numpy as np

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        last_index = len(nums) - 1
        location = 0
        while True:
            remain_steps = nums[location]
            if remain_steps == 0:
                return False
            if location + remain_steps >= last_index:
                return True
            possible_choices = nums[location+1: location+remain_steps+1]
            dist_expectation = np.asarray(list(map(lambda x,y: x+y, possible_choices, range(-(last_index-location-1),1))))
            optimized_steps = np.max(dist_expectation)
            
            # np.where returns tuple, get farest position
            dist_to_maximize_steps = np.where(dist_expectation==optimized_steps)[0][-1].item() + 1
            location += dist_to_maximize_steps

if __name__ == '__main__':
    
    nums = [2,3,1,1,4]
    expected = True
    
    nums = [0]
    expected = True
    
    print(f'nums: {nums}')
    print(f'exptected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.canJump(nums))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 2397 ms, faster than 15.49% of Python3 online submissions for Jump Game.
Memory Usage: 31.7 MB, less than 5.23% of Python3 online submissions for Jump Game.
"""