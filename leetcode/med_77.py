"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

E.g.1
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

E.g.2
Input: n = 1, k = 1
Output: [[1]]
"""
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        if k > n//2:
            combines = self.combines(list(range(1,n+1)), n-k)
            if not combines:
                return [list(range(1,n+1))]
            return [ [j for j in range(1,n+1) if j not in combine] for combine in combines]
        
        return self.combines(list(range(1,n+1)), k)
    
    def combines(self, nums, k):
        n = len(nums)
        if not nums or k == 0 or k > n:
            return []
        if k == 1:
            return [ [num] for num in nums ]
        return [ [nums[j], *combine] for j in range(n) for combine in self.combines(nums[j+1:], k-1)]
            

if __name__ == '__main__':
    
    n = 16
    k = 15
    
    print(f'n: {n}, k: {k}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.combine(n, k))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 128 ms, faster than 80.82% of Python3 online submissions for Combinations.
Memory Usage: 16.4 MB, less than 7.78% of Python3 online submissions for Combinations.
"""