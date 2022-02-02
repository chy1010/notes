"""
Implement next permutation, which rearranges numbers into
the lexicographically next greater permutation of numbers.
If such an arrangement is impossible, it must rearrange it
to the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

E.g.1:
Input: nums = [1,2,3]
Output: [1,3,2]

E.g.2:
Input: nums = [3,2,1]
Output: [1,2,3]

E.g.3:
Input: nums = [1,1,5]
Output: [1,5,1]
"""
from itertools import permutations
import numpy as np
from typing import List

class Solution:
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        1 4 1 5 4 3 2 1
        """
        n = len(nums)
        if n == 2:
            nums[::] = nums[::-1]
            return 
        reverse_ind = self.return_non_increaing_index(nums)
        if reverse_ind == -1:
            nums[::] = nums[::-1]
        else:
            for j in range(reverse_ind+1, n+1):
                if j == n:
                    break
                if nums[j] <= nums[reverse_ind]:
                    break
            nums[reverse_ind], nums[j-1] = nums[j-1], nums[reverse_ind]
            nums[reverse_ind+1:] = nums[reverse_ind+1:][::-1]
        
    def return_non_increaing_index(self, numbers):
        previous = numbers[-1]
        for j in range(len(numbers)-2,-1,-1):
            if previous > numbers[j]:
                return j
            previous = numbers[j]
        return -1
        
            
        
    
    def brute_force(self, nums):
        
        original_num = int(''.join(f'{j:03d}' for j in nums))
        perms = permutations(nums)
        num_list = []
        for num in perms:
            this_term = int(''.join(f'{j:03d}' for j in num))
            num_list.append(this_term)
        num_list = sorted(num_list)
        for this_term in num_list:
            if this_term > original_num:
                output = str(this_term) + ' '
                outputs = list()
                length = int(np.ceil(len(output) / 3))
                for j in range(length):
                    outputs.append(int(output[-3*(j+1)-1:-3*j-1]))
                outputs = outputs[::-1]
                return outputs
        this_term = num_list[0]
        output = str(this_term) + ' '
        outputs = list()
        length = int(np.ceil(len(output) / 3))
        for j in range(length):
            outputs.append(int(output[-3*(j+1)-1:-3*j-1]))
        outputs = outputs[::-1]
        return outputs

if __name__ == '__main__':
    
    nums = [1,2,3]
    nums = [3,2,1]
    nums = [1,3,2]
    nums = [1,2]
    
    print(f'nums: {nums}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    print(f'expected: {sol.brute_force(nums)}')
    print(f'time duration: {time() - start}')
    
    start = time()
    sol.nextPermutation(nums)
    print(f'solution: {nums}')
    
    print(f'time duration: {time() - start}')
    
"""
Runtime: 48 ms, faster than 27.21% of Python3 online submissions for Next Permutation.
Memory Usage: 14.3 MB, less than 20.66% of Python3 online submissions for Next Permutation.
"""