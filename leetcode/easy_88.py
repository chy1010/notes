"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.

To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored.

nums2 has a length of n.

 

E.g.1
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

E.g.2
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

E.g.3
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not (m+n):
            return True
        if not m:
            nums1[:] = nums2
            return True
        if not n:
            return True
        
        # nums1[m:] = nums2
        # nums1.sort()
        nums1[n:] = nums1[:m]
        
        i = n
        j = 0
        while i < m+n and j < n:
            if nums1[i] < nums2[j]:
                nums1[i+j-n] = nums1[i]
                i+=1
            else:
                nums1[i+j-n] = nums2[j]
                j+=1
        if i == m+n:
            nums1[i+j-n:] = nums2[j:]
        
                
            

if __name__ == '__main__':
    
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    o = [1,2,2,3,5,6]
    
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    o = [1]
    
    print(f'nums1: {nums1}, m: {m}; nums2: {nums2}; n: {n}')
    print(f'o: {o}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    sol.merge(nums1, m, nums2, n)
    print(nums1)
    
    print(f'time duration: {time() - start}')

"""
Runtime: 56 ms, faster than 25.51% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.3 MB, less than 32.63% of Python3 online submissions for Merge Sorted Array.
Runtime: 70 ms, faster than 8.45% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.4 MB, less than 32.63% of Python3 online submissions for Merge Sorted Array.
"""