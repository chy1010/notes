"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

E.g.1
nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

E.g.2
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

E.g.3
Input: nums = [], target = 0
Output: [-1,-1]
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.partial_search(nums, target)

    def partial_search(self, nums, target):
        if not nums:
            return [-1, -1]
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        half = n // 2
        left_inds = self.partial_search(nums[:half], target)
        right_inds = self.partial_search(nums[half:], target)
        if left_inds == [-1, -1]:
            if right_inds == [-1, -1]:
                return [-1, -1]
            return [right_ind + half for right_ind in right_inds]
        if right_inds == [-1, -1]:
            return left_inds
        return [left_inds[0], right_inds[1]+half]
            


if __name__ == '__main__':
    
    nums = [5,7,7,8,8,10]
    target = 6
    expected = [-1,-1]
    
    nums = [5,7,7,8,8,10]
    target = 8
    expected = [3,4]
    
    
    
    
    print(f'nums: {nums}; target: {target}')    
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.searchRange(nums, target))
    
    print(f'time duration: {time() - start}')
    
"""
Runtime: 132 ms, faster than 13.32% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.5 MB, less than 54.80% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""