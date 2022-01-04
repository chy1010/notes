"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.

The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.

More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.

E.g.1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

E.g.2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 0
        previous = -101
        while len(nums):
            head = nums.pop(0)
            if head > previous:
                nums.append(head)
                k+=1
                previous = head
            elif head == previous:
                continue
            else:
                break
        nums.insert(0, head)
        return k

if __name__ == '__main__':
    
    nums = [1,1,2]
    expected = 1
    
    print(f'nums: {nums}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    k = sol.removeDuplicates(nums)
    print(f'time duration: {time() - start}')
    print(k, end=', ')
    print(nums)


"""
Runtime: 232 ms, faster than 6.02% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.7 MB, less than 47.26% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""