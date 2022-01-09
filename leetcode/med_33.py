"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated
at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is

[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

E.g.1
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

E.g.2
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

E.g.3
Input: nums = [1], target = 0
Output: -1
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.partial_search(nums, target)
    
    def partial_search(self, nums, target):
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        half = n // 2
        left_ind = self.partial_search(nums[:half], target)
        right_ind = self.partial_search(nums[half:], target)
        if left_ind == -1:
            if right_ind == -1:
                return -1
            return right_ind+half
        return left_ind
        

if __name__ == '__main__':
    
    nums = [4,5,6,7,0,1,2]
    target = 0
    expected = 4
    
    nums = [4,5,6,7,0,1,2]
    target = 3
    expected = -1
    
    nums = [1]
    target = 0
    expected = -1
    
    print(f'nums: {nums}; target: {target}')    
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.search(nums, target))
    print(f'time duration: {time() - start}')

"""
Runtime: 44 ms, faster than 53.61% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.7 MB, less than 56.27% of Python3 online submissions for Search in Rotated Sorted Array.
"""