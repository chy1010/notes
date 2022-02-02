"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

E.g.1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

E.g.2:
Input: strs = [""]
Output: [[""]]

E.g.3:
Input: strs = ["a"]
Output: [["a"]]
"""
from typing import List
# from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []
        self.hash_table = defaultdict(list)
        _ = list(map(self.hashing, strs))
        # for string in strs:
        #     self.hashing(string)
        # with ThreadPoolExecutor(max_workers=8) as executor:
        #     _ = list(executor.map(self.hashing, strs, chunksize=2))
        return list(self.hash_table.values())
    
    def hashing(self, string):
        key = ''.join(sorted(string))
        self.hash_table[key].append(string)
        

if __name__ == '__main__':
    
    strs = ["eat","tea","tan","ate","nat","bat"]
    expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    strs = [""]
    expected = [[""]]
    
    strs = ["a"]
    expected = [["a"]]
    
    print(f'strs: {strs}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.groupAnagrams(strs))
    
    print(f'time duration: {time() - start}')


"""
Runtime: 142 ms, faster than 28.24% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.8 MB, less than 57.77% of Python3 online submissions for Group Anagrams.
"""