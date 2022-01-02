"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        if n == 1:
            return ['()']
        n=n*2
        
        rets = self.generate_sub_parenthesis(n-1, 1)
        rets = ['('+ret for ret in rets]
        return rets
    
    def generate_sub_parenthesis(self, n, temp) -> List[str]:
        if n == temp:
            return [')'*n]
        ret1 = self.generate_sub_parenthesis(n-1, temp+1)
        ret1 = ['('+ret for ret in ret1]
        if temp > 0:
            ret2 = self.generate_sub_parenthesis(n-1, temp-1)
            ret2 = [')'+ret for ret in ret2]
            ret1.extend(ret2)
        return ret1
            

if __name__ == '__main__':
    
    n = 3
    expected = ["((()))","(()())","(())()","()(())","()()()"]
    
    # n = 1
    # expected = ["()"]
    
    n = 4
    expected = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    
    print(f'n={n}')
    print(f'expected=\n{expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.generateParenthesis(n))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 36 ms, faster than 66.63% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.6 MB, less than 68.44% of Python3 online submissions for Generate Parentheses.
"""