class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        if s == '':
            return True
        else:
            return False
        
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