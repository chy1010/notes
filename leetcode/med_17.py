"""
Given a string containing digits from 2 - 9 inclusive, return all possible letter combinations
that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]
"""
from typing import List
from itertools import product

class Solution:
    rep = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    def letterCombinations(self, digits: str) -> List[str]:
        choices = [self.rep[d] for d in digits]
        print(choices)
        cbtns = [''.join(letters) for letters in product(*choices) if letters]
        return cbtns


if __name__ == '__main__':
    
    sol = Solution()
    sol.letterCombinations('')