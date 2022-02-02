"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

E.g.1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

E.g.2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda k: (k[0], k[1]))
        return self.merge_intervals(intervals)
    
    def merge_intervals(self, intervals):
        n = len(intervals)
        if n == 1:
            return intervals
        if n == 2:
            I1, I2 = intervals
            if I1[1] >= I2[0]:
                return [[I1[0], max(I2[1], I1[1])]]
            return intervals
        half = n // 2
        left_intervals = self.merge_intervals(intervals[:half])
        right_intervals = self.merge_intervals(intervals[half:])
        left_end = left_intervals[-1][1]
        for j in range(len(right_intervals)+1):
            # if left_end >= right_intervals[j][0]:
            #     continue
            if j == len(right_intervals) or left_end < right_intervals[j][0]:
                break
            
        if j > 0:
            # cover the first j-1 interval, 
            # since intervals in both left and right must be disjoint.
            left_intervals[-1][1] = max(right_intervals[j-1][1], left_end)
            right_intervals = right_intervals[j:]
        return [*left_intervals, *right_intervals]
            

if __name__ == '__main__':
    
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    expected = [[1,6],[8,10],[15,18]]
    
    # intervals = [[1,4],[4,5]]
    # expected = [[1,5]]
    
    # intervals = [[1,4],[5,6]]
    # expected = [[1,4],[5,6]]
    
    intervals = [[1,4],[2,3]]
    expected = [[1,4]]
    
    intervals = [[2,3],[5,5],[2,2],[3,4],[3,4]]
    expected = [[2,4],[5,5]]
    
    # import json
    # with open('leetcode/test-data/med_56_data.json', mode='r') as fp:
    #     intervals = json.load(fp)
    # expected = None
    
    intervals = [[1,4],[0,2],[3,5]]
    expected = [[0,5]]
    
    print(f'intervals: {intervals}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.merge(intervals))
    
    print(f'time duration: {time() - start}')


"""
Runtime: 164 ms, faster than 20.17% of Python3 online submissions for Merge Intervals.
Memory Usage: 18.6 MB, less than 8.32% of Python3 online submissions for Merge Intervals.
"""