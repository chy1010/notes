"""
Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.

More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        if val not in nums:
            return len(nums)
        
        fast = 0
        while fast < len(nums):
            if nums[fast] == val:
                break
            fast += 1
        slow = fast
        fast += 1
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        return slow

if __name__ == '__main__':
    
    nums = [3,2,2,3]
    val = 3
    expected = 2 #nums = [2,2,_,_]
    
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    expected = 5 # nums = [0,1,4,0,3,_,_,_]
    
    print(f'nums: {nums}')
    print(f'val: {val}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    k = sol.removeElement(nums=nums, val=val)
    print(f'time duration: {time() - start}')
    
    print(k, end=', ')
    print(nums)


"""
完全沒改, 重新 submit.... 靠運氣才在 28 ms 內完成.
Runtime: 28 ms, faster than 92.82% of Python3 online submissions for Remove Element.
Memory Usage: 14.5 MB, less than 13.73% of Python3 online submissions for Remove Element.

Runtime: 53 ms, faster than 8.57% of Python3 online submissions for Remove Element.
Memory Usage: 14.1 MB, less than 91.73% of Python3 online submissions for Remove Element.
"""