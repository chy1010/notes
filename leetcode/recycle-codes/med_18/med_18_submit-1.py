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
from collections import defaultdict
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        storage = defaultdict(int)
        def counter(num):
            storage[num]+=1
            return storage[num]
        nums.sort()
        nums = [num for num in nums if counter(num) <= 4]
        # print(nums)
        # raise 'Stop'
        
        final_results = []
        while len(nums) >= 4:
            head = nums.pop(0)
            if 4 * head == target and storage[head] >= 4:
                final_results.append([head]*4)
                break
            two_sum_results = []
            three_sum_results = []
            if nums[0] == head:
                # repeats 2 times
                nums.pop(0)
                if nums[0] == head:
                    # repeats 3 times
                    nums.pop(0)
                    if nums[0] == head:
                        # repeats 4 times
                        nums.pop(0)
                    if target - 3 * head in nums:
                        final_results.append([head, head, head, target-3*head])
                two_sum_results = self.check_two_sum(nums, target=target-2*head)
                if two_sum_results:
                    two_sum_results = [ [head, head, *result] for result in two_sum_results]
                    
            three_sum_results = self.check_three_sum(nums, target=target-head)
            if three_sum_results:
                three_sum_results = [ [head, *result] for result in three_sum_results]
            final_results.extend(two_sum_results)
            final_results.extend(three_sum_results)
        return final_results
        
    def check_three_sum(self, nums: List[int], target: int):
        complete = []
        right_edge = len(nums) - 1
        for j in range(right_edge - 1):
            if (3*nums[j] > target) or (3*nums[right_edge] < target):
                break
            if j > 0 and (nums[j-1] == nums[j]):
                continue

            i = j + 1
            k = right_edge
            while i < k:
                three_sum = nums[j] + nums[i] + nums[k]
                if three_sum == target:
                    if (len(complete) == 0) or (complete[-1] != [nums[j], nums[i], nums[k]]):
                        complete.append([nums[j], nums[i], nums[k]])
                        if i == j+1:
                            right_edge = k-1
                    i+=1
                    k-=1
                elif three_sum > target:
                    if i == j+1:
                        right_edge = k-1
                    k-=1
                else: # three_sum < target:
                    i+=1

        return complete
    
    def check_two_sum(self, nums, target):
        n = len(nums)
        if n < 2:
            return []
        results = []
        p = None
        for i in range(n-1):
            if p is None or nums[i] > p:
                if target - nums[i] in nums[i+1:]:
                    results.append([nums[i], target-nums[i]])
                    p = nums[i]
        return results
                
        
            
        

if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    target = 0
    expected = None
    
    nums = [2,2,2,2,2]
    target = 8
    expected = [[2,2,2,2]]
    
    
    # nums = [-5,-4,-3,-2,-1,0,0,1,2,3,4,5]
    # target = 0
    # expected = [[-5,-4,4,5],[-5,-3,3,5],[-5,-2,2,5],[-5,-2,3,4],[-5,-1,1,5],[-5,-1,2,4],[-5,0,0,5],[-5,0,1,4],[-5,0,2,3],[-4,-3,2,5],[-4,-3,3,4],[-4,-2,1,5],[-4,-2,2,4],[-4,-1,0,5],[-4,-1,1,4],[-4,-1,2,3],[-4,0,0,4],[-4,0,1,3],[-3,-2,0,5],[-3,-2,1,4],[-3,-2,2,3],[-3,-1,0,4],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    
    # nums = [-1,2,2,-5,0,-1,4]
    # target = 3
    # expected = [[-5,2,2,4],[-1,0,2,2]]
    
    # nums = [0,-1,0,1,-2,-5,3,5,0]
    # target = 6
    # expected = [[-2,0,3,5],[0,0,1,5]]
    
    
    # nums = [1,-5,-1,1,-6,-7,-5,-1,-1,2,-5,6,4,5,-8,1,3,-1,9]
    # target = 0
    # expected = [[-8,-7,6,9],[-8,-6,5,9],[-8,-5,4,9],[-8,-1,3,6],[-8,-1,4,5],[-8,1,1,6],[-8,1,2,5],[-8,1,3,4],[-7,-6,4,9],[-7,-5,3,9],[-7,-1,-1,9],[-7,-1,2,6],[-7,-1,3,5],[-7,1,1,5],[-7,1,2,4],[-6,-5,2,9],[-6,-5,5,6],[-6,-1,1,6],[-6,-1,2,5],[-6,-1,3,4],[-6,1,1,4],[-6,1,2,3],[-5,-5,1,9],[-5,-5,4,6],[-5,-1,1,5],[-5,-1,2,4],[-5,1,1,3],[-1,-1,-1,3],[-1,-1,1,1]]
    
    print(f'nums: {sorted(nums)}')
    print(f'target: {target}')
    if expected is not None:
        print(f'expected:')
        print(expected)
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    print(sol.fourSum(nums, target))
    print(f'time duration: {time() - start}')