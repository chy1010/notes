"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
"""
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        return self.calculate_sum(candidates, target)
    
    def calculate_sum(self, candidates, target):
        first_candy = candidates[0]
        if first_candy > target:
            return []
        elif first_candy == target:
            return [[target]]
        n = len(candidates)
        if n == 1:
            return []
        counts = 1
        j = 1
        while j < n:
            if candidates[j] > first_candy:
                break
            counts += 1
            j += 1
        outputs = []
        if j < n and target >= candidates[j]:
            outputs.extend(self.calculate_sum(candidates[j:], target))
        rounds = min(target // first_candy, counts)
        res = target
        mul = 0
        while mul < rounds and res > first_candy:
            res -= first_candy
            mul += 1
            if j < n and res >= candidates[j]:
                this_output = self.calculate_sum(candidates[j:], res)
                this_output = [ [*([first_candy]*mul), *that_output] for that_output in this_output]
                outputs.extend(this_output)
        if res == first_candy and mul < rounds:
            outputs.append([first_candy]*(mul+1))
        return outputs

if __name__ == '__main__':
    
    
    candidates = [10,1,2,7,6,1,5]
    target = 8
    
    candidates = [2,5,2,1,2]
    target = 5
    
    # candidates = [1,2]
    # target = 2

    print(f'candidates: {candidates}')
    print(f'target: {target}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.combinationSum2(candidates, target))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 71 ms, faster than 65.66% of Python3 online submissions for Combination Sum II.
Memory Usage: 14.5 MB, less than 20.80% of Python3 online submissions for Combination Sum II.
"""