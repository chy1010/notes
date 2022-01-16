"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

E.g.1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

E.g.2:
Input: nums = [0]
Output: [[],[0]]
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        n = len(nums)
        return [ set for k in range(n+1) for set in self.select_subset(nums, k) ]

    def select_subset(self, nums, k):
        n = len(nums)
        if k == 0:
            return [[]]
        if n == 0 or k > n:
            return []
        if k == 1:
            return [[num] for num in nums]
        return [ [nums[j], *combine] for j in range(n) for combine in self.select_subset(nums[j+1:], k-1)]

if __name__ == '__main__':
    
    nums = [1,2,3]
    o = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    
    print(f'nums: {nums}')
    print(f'o: {o}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.subsets(nums))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 36 ms, faster than 66.30% of Python3 online submissions for Subsets.
Memory Usage: 14.7 MB, less than 18.31% of Python3 online submissions for Subsets.
"""