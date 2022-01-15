"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
    "123", "132", "213", "231", "312", "321"
Given n and k, return the kth permutation sequence.

E.g.1:
Input: n = 3, k = 3
Output: "213"

E.g.2:
Input: n = 4, k = 9
Output: "2314"

E.g.3:
Input: n = 3, k = 1
Output: "123"
"""
from functools import reduce

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return '12' if k==1 else '21'
        
        DIGITS = {i: str(i+1) for i in range(9)}
        np1_perm_num = reduce(lambda a, b: a*b, range(1,n))
        first_digit_num = k // np1_perm_num if k % np1_perm_num != 0 else k // np1_perm_num - 1
        first_digit = DIGITS[first_digit_num]
        remain_digit_num = k % np1_perm_num if k % np1_perm_num != 0 else np1_perm_num
        remain_digits = self.getPermutation(n-1, remain_digit_num)
        for j in range(n, first_digit_num+1, -1):
            remain_digits = remain_digits.replace(f'{j-1}', f'{j}')
        return first_digit + remain_digits
        
        

if __name__ == '__main__':
    
    
    n = 4
    k = 9
    expected = "2314"
    
    # n = 3
    # k = 1
    # expected = "123"
    
    n = 3
    k = 3
    expected = "213"

    
    print(f'n: {n}; k: {k}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.getPermutation(n,k))
    
    
    print(f'time duration: {time() - start}')


"""
Runtime: 49 ms, faster than 32.30% of Python3 online submissions for Permutation Sequence.
Memory Usage: 14.1 MB, less than 87.73% of Python3 online submissions for Permutation Sequence.
"""