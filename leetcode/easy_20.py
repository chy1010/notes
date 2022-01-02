"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        memo = []
        left = ['{', '[', '(']
        right_to_left = {'}': '{', ')': '(', ']': '['}
        
        while len(s) > 0:
            c, s = s[0], s[1:]
            if c in left:
                memo.append(c)
            else:
                if len(memo) > 0 and right_to_left[c] == memo[-1]:
                    memo.pop(-1)
                else:
                    return False
        if len(memo) > 0:
            return False
        return True

if __name__ == '__main__':
    
    s = "()"
    expected = True
    
    # s = "()[]{}"
    # expected = True
    
    # s = "(]"
    # expected = False
    
    s = "{[]}"
    expected = True
    
    # s = "()"
    # expected = True
    
    # s = "]"
    # expected = False
    
    print(f's: {s}')
    print(f'expected: {expected}')
    print('-'*30)
    
    sol = Solution()
    from time import time
    start = time()
    print(sol.isValid(s))
    print(f'time duration: {time() - start}')


"""
Runtime: 59 ms, faster than 5.28% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.4 MB, less than 36.13% of Python3 online submissions for Valid Parentheses.
"""