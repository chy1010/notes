"""
You are given an array of non-overlapping intervals intervals
where intervals[i] = [starti, endi] represent the start and the end of the ith interval
and intervals is sorted in ascending order by starti.

You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion. 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        n = len(intervals)
        if n == 1:
            a, b = newInterval
            c, d = intervals[0]
            if b < c:
                return [[a,b], [c,d]]
            elif d < a:
                return [[c,d], [a,b]]
            return [[min(a,c), max(b,d)]]
        self.intervals = intervals
        i = 0
        j = n-1
        a, b = newInterval
        
        if a > intervals[-1][1]:
            intervals.append([a,b])
            return intervals
        elif b < intervals[0][0]:
            intervals.insert(0, [a,b])
            return intervals
        
        if a < intervals[0][0]:
            left_index = (-1, 0)
        else:
            left_index = self.insert_index(i, j, a)
        if b > intervals[-1][1]:
            right_index = (n-1,n)
        else:
            right_index = self.insert_index(left_index[0], j, b)
        
        if len(left_index) == 1:
            new_interval_left_end = min(intervals[left_index[0]][0], a)
            left_part = left_index[0] - 1
        else:
            new_interval_left_end = a
            left_part = left_index[0]
            
        if len(right_index) == 1:
            new_interval_right_end = max(intervals[right_index[0]][1], b)
            right_part = right_index[0] + 1
        else:
            new_interval_right_end = b
            right_part = right_index[1]
            
        new_interval = [new_interval_left_end, new_interval_right_end]
        new_intervals = [
            *intervals[:left_part+1],
            new_interval,
            *intervals[right_part:]
        ]
        return new_intervals
    
    def insert_index(self, i, j, num):
        if i == j - 1:
            if self.intervals[i][0] <= num <= self.intervals[i][1]:
                return (i, )
            elif self.intervals[i][1] < num < self.intervals[j][0]:
                return (i, j)
            else:
                return (j, )
        half = (i+j) // 2
        if self.intervals[half][0] <= num <= self.intervals[half][1]:
            return (half, )
        elif num < self.intervals[half][0]:
            return self.insert_index(i, half, num)
        else:
            return self.insert_index(half, j, num)

if __name__ == '__main__':
    
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    expected = [[1,5],[6,9]]
    
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    expected = [[1,2],[3,10],[12,16]]
    
    intervals = [[1,5],[6,8]]
    newInterval = [0,9]
    expected = [[0,9]]
    
    print(f'intervals: {intervals}, newInterval: {newInterval}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.insert(intervals, newInterval))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 100 ms, faster than 31.91% of Python3 online submissions for Insert Interval.
Memory Usage: 17.6 MB, less than 32.91% of Python3 online submissions for Insert Interval.
"""