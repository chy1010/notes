"""
Given a string s consisting of some words separated by some number of spaces,
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

E.g.1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

E.g.2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

E.g.3
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.lstrip().rstrip()
        ret = s.split()[-1]
        return len(ret)

if __name__ == '__main__':
    
    s = "Hello World"
    expected = 5
    
    print(f's: {s}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.lengthOfLastWord(s))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 50 ms, faster than 14.04% of Python3 online submissions for Length of Last Word.
Memory Usage: 14.2 MB, less than 87.27% of Python3 online submissions for Length of Last Word.
"""