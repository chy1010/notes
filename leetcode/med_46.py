"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

E.g.1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

E.g.2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

E.g.3:
Input: nums = [1]
Output: [[1]]
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [nums]
        elif n == 2:
            return [nums, nums[::-1]]
        
        outputs = [ [nums[0], *np1_perm ] for np1_perm in self.permute(nums[1:]) ]
        for j in range(1, n):
            nums[0], nums[j] = nums[j], nums[0]
            outputs.extend([ [nums[0], *np1_perm] for np1_perm in self.permute(nums[1:]) ])
        return outputs

if __name__ == '__main__':
    
    nums = [1,2,3]
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    
    nums = [0,1]
    expected = [[0,1],[1,0]]
    
    nums = [1]
    expected = [[1]]
    
    print(f'nums: {nums}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.permute(nums))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 40 ms, faster than 74.73% of Python3 online submissions for Permutations.
Memory Usage: 14.6 MB, less than 14.92% of Python3 online submissions for Permutations.
"""