"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

E.g.1
Input: nums = [1,3,5,6], target = 5
Output: 2

E.g.2
Input: nums = [1,3,5,6], target = 2
Output: 1

E.g.3
Input: nums = [1,3,5,6], target = 7
Output: 4
"""
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.find_insert_index(nums, target)
    
    def find_insert_index(self, nums, target):
        n = len(nums)
        left = 0
        right = n
        while left < right - 1:
            half = (right + left) // 2
            # print(f'left: {left}, half: {half}, right: {right}')
            if nums[half] == target:
                return half
            elif nums[half] > target:
                right = half
            else: #  nums[half] < target:
                left = half
        if nums[left] >= target:
            return left
        return right
            
            
        

if __name__ == '__main__':
    
    nums = [1,3,5,6]
    target = 5
    expected = 2
    
    nums = [1,3,5,6]
    target = 2
    expected = 1
    
    # nums = [1,3,5,6]
    # target = 7
    # expected = 4
    
    # nums = [1,3,5,6]
    # target = 0
    # expected = 0
    
    print(f'nums: {nums}, target: {target}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.searchInsert(nums, target))
    
    print(f'time duration: {time() - start}')
    
"""
Runtime: 64 ms, faster than 26.59% of Python3 online submissions for Search Insert Position.
Memory Usage: 15.2 MB, less than 24.05% of Python3 online submissions for Search Insert Position.
"""