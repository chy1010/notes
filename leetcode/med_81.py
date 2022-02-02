"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function,
nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that
the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target,
return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

E.g.1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

E.g.2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 1:
            return nums[0] == target
        
        left_end = nums[0]
        right_end = nums[-1]
        # number less than or equal to right_end must be left part
        # number less than or equal to left_end must be right part
        
        if target == left_end or target == right_end:
            return True
        
        for i in range(n):
            if nums[i] != left_end:
                break
            
        for j in range(n-1,-1,-1):
            if nums[j] != right_end:
                break
        nums = nums[i:j+1]
        n = len(nums)
        if not n: 
            return False
        if n == 1:
            return nums[0] == target
        
        i = 0
        j = n-1
        
        if nums[0] >= nums[-1]:        
            while i < j - 1:
                half = (i+j) // 2
                if nums[half] < right_end:
                    j = half
                elif nums[half] > left_end:
                    i = half

            if target > nums[i] or target < nums[j]:
                return False
            if target <= nums[-1]:
                i = i+1
                j = n-1
            elif target >= nums[0]:
                j = i
                i = 0
            
        while i < j - 1:
            half = (i+j) // 2
            if target == nums[half]:
                return True
            elif target > nums[half]:
                i = half
            else: # target < nums[half]
                j = half

        return (target == nums[i]) or (target == nums[j])
            
        

if __name__ == '__main__':
    
    nums = [2,5,6,0,0,1,2]
    target = 0
    o = True
    
    nums = [2,5,6,0,0,1,2]
    target = 3
    o = False
    
    nums = [1,1]
    target = 0
    o = False
    
    nums = [4,5,6,7,0,1,2]
    target = 1
    o = True
    
    nums = [0,0,1,1,2,0]
    target = 2
    o = True
    
    # nums = [1,0,1,1,1]
    # target = 0
    # o = True
    
    print(f'nums: {nums}, target: {target}')
    
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.search(nums, target))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 94 ms, faster than 11.93% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 15.1 MB, less than 33.20% of Python3 online submissions for Search in Rotated Sorted Array II.
"""