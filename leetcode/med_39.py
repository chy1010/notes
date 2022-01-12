"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        return self.calculate_sum(candidates, target)
    
    def calculate_sum(self, candidates, target):
        n = len(candidates)
        if n == 1:
            if target % candidates[0] == 0:
                return [[candidates[0]] * (target // candidates[0])]
            else:
                return []
        num = candidates[0]
        res = target
        outputs = self.calculate_sum(candidates[1:], target)
        mul = 0
        while res > num:
            res -= num
            mul += 1
            if res >= candidates[1]:
                this_output = self.calculate_sum(candidates[1:], res)
                this_output = [ [*([num]*mul), *that_output] for that_output in this_output]
                outputs.extend(this_output)
        if res == num:
            outputs.append([num]*(mul+1))
        return outputs

if __name__ == '__main__':
    
    candidates = [2,3,6,7]
    target = 7
    expected = [[2,2,3],[7]]
    
    candidates = [2,3,5]
    target = 8
    expected = [[2,2,2,2],[2,3,3],[3,5]]
    
    # candidates = [2]
    # target = 1
    # expected = []
    
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.combinationSum(candidates, target))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 104 ms, faster than 42.99% of Python3 online submissions for Combination Sum.
Memory Usage: 14.3 MB, less than 52.55% of Python3 online submissions for Combination Sum.
"""