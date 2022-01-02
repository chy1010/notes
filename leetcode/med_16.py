"""
Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

E.g.1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

E.g.2:
Input: nums = [0,0,0], target = 1
Output: 0
"""
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        now_dist = 1e8
        now_value = None
        nums.sort()
        right_edge = len(nums) - 1
        for j in range(right_edge - 1):
            if ( (3*nums[j] - target) > now_dist) or ( (target - 3*nums[right_edge]) > now_dist ):
                break
            if j > 0 and (nums[j-1] == nums[j]):
                continue

            i = j + 1
            k = right_edge
            while i < k:
                three_sum = nums[j] + nums[i] + nums[k]
                # print(f'{nums[j]} + {nums[i]} + {nums[k]} = {three_sum}')
                if three_sum == target:
                    return target
                elif three_sum > target:
                    if three_sum - target < now_dist:
                        now_dist = three_sum - target
                        now_value = three_sum
                    if i == j+1:
                        right_edge = k-1
                    k-=1
                else: # three_sum < target:
                    if target - three_sum < now_dist:
                        now_dist = target - three_sum
                        now_value = three_sum
                    i+=1
        return now_value
    
    
if __name__ == '__main__':
    
    nums = [0,0,0]
    target = 1
    expected = None
    
    nums = [-1,2,1,-4]
    target = 1
    expected =  2
    
    nums = [3,3,4,5,6,7,8,-1,-3,-5]
    target = 6
    expected = 6
    
    print(f'nums: {sorted(nums)}')
    print(f'target: {target}')
    if expected is not None:
        print(f'expected:')
        print(expected)
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    print(sol.threeSumClosest(nums, target))
    print(f'time duration: {time() - start}')