"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Eg1.
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Eg2.
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

"""
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        final_results = []
        while len(nums) >= 4:
            head = nums.pop(0)
            results = self.check_three_sum(nums, target=target-head)
            if results:
                results = [ [head, *result] for result in results]
            final_results.extend(results)
        clean_results = []
        for result in final_results:
            if result in clean_results:
                continue
            clean_results.append(result)
        final_results = clean_results
        return final_results
        
    def check_three_sum(self, nums: List[int], target: int):
        n = len(nums)
        if n < 3:
            return []
        
        right_end = n - 1
        results = []
        for i in range(n-2):
            p = nums[i]
            k = right_end
            j = i+1
            while j < k:
                three_sum = p + nums[j] + nums[k]
                if three_sum == target:
                    if len(results) == 0 or (results[-1] != [p, nums[j], nums[k]]):
                        results.append([p, nums[j], nums[k]])
                    j+=1
                    k-=1
                elif three_sum > target:
                    if j == i+1:
                        right_end = k-1
                    k-=1
                else: # three_sum < target
                    j += 1
        return results
        
            
        

if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    target = 0
    
    nums = [2,2,2,2,2]
    target = 8
    
    print(f'nums: {sorted(nums)}')
    print(f'target: {target}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    print(sol.fourSum(nums, target))
    print(f'time duration: {time() - start}')