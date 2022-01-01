"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

E.g.1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

E.g.2:
Input: nums = []
Output: []

E.g.3:
Input: nums = [0]
Output: []
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        complete = []
        nums.sort()
        right_edge = len(nums) - 1
        for j in range(right_edge - 1):
            if (nums[j] > 0) or (nums[right_edge] < 0):
                break
            if j > 0 and (nums[j-1] == nums[j]):
                continue

            i = j + 1
            k = right_edge
            while i < k:
                sum = nums[j] + nums[i] + nums[k]
                if sum == 0:
                    if (len(complete) == 0) or (complete[-1] != [nums[j], nums[i], nums[k]]):
                        complete.append([nums[j], nums[i], nums[k]])
                        if i == j+1:
                            right_edge = k-1
                    i+=1
                    k-=1
                elif sum > 0:
                    if i == j+1:
                        right_edge = k-1
                    k-=1
                else: # sum < 0
                    i+=1

        return complete
    
if __name__ == '__main__':
    
    nums = [-1,0,1,2,-1,-4]
    sol = Solution()
    from time import time
    start_time = time()
    print(sol.threeSum(nums))
    print(f'time duration: {time() - start_time}')
    
    