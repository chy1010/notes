"""
Given a collection of numbers, nums, that might contain duplicates, 
eturn all possible unique permutations in any order.

E.g.1:
Input: nums = [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]

E.g.2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [nums]
        elif n == 2:
            if nums[0] != nums[1]:
                return [nums, nums[::-1]]
            else:
                return [nums]
        
        outputs = [ [nums[0], *np1_perm ] for np1_perm in self.permuteUnique(nums[1:]) ]
        register = set([nums[0]])
        for j in range(1, n):
            nums[0], nums[j] = nums[j], nums[0]
            if nums[0] in register:
                continue
            else:
                register.add(nums[0])
            outputs.extend([ [nums[0], *np1_perm] for np1_perm in self.permuteUnique(nums[1:]) ])
        return outputs

if __name__ == '__main__':
    
    nums = [1,1,2]
    expected = [[1,1,2], [1,2,1], [2,1,1]]
    
    # nums = [1,2,3]
    # expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    
    print(f'nums: {nums}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    
    
    print(f'time duration: {time() - start}')

"""
Runtime: 65 ms, faster than 51.27% of Python3 online submissions for Permutations II.
Memory Usage: 14.6 MB, less than 62.41% of Python3 online submissions for Permutations II.
"""