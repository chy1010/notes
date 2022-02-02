"""
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

 
E.g.1
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

E.g.2
Input: nums = [2,0,1]
Output: [0,1,2]
"""
from typing import List
from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = dict(Counter(nums))
        counter.update({i: 0 for i in range(3) if i not in counter})
        nums[:counter[0]] = [0]*counter[0]
        nums[counter[0]:counter[0]+counter[1]] = [1]*counter[1]
        nums[counter[0]+counter[1]:] = [2]*counter[2]
        

if __name__ == '__main__':
    
    nums = [2,0,2,1,1,0]
    o = [0,0,1,1,2,2]
    
    nums = [1]
    o = [1]
    
    print(f'nums: {nums}')
    print(f'o: {o}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    sol.sortColors(nums)
    print(nums)
    
    print(f'time duration: {time() - start}')

"""
Runtime: 56 ms, faster than 14.75% of Python3 online submissions for Sort Colors.
Memory Usage: 14.5 MB, less than 13.27% of Python3 online submissions for Sort Colors.
"""