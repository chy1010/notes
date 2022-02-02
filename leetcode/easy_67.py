"""
Given two binary strings a and b, return their sum as a binary string.

E.g.1:
Input: a = "11", b = "1"
Output: "100"

E.g.2:
Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)
        n = len(b)
        carry = '0'
        output = []
        for j in range(1, min(m,n)+1):
            binary_sum = sum([1 for c in [a[-j], b[-j], carry] if c == '1'])
            carry = '1' if binary_sum // 2 else '0'
            output.append(str(binary_sum % 2))
        prefix = a[:-min(m,n)] or b[:-min(m,n)]
        if carry == '1':
            prefix = self.addOne(prefix)
        return prefix + ''.join(output[::-1])
        
    def addOne(self, d: str):
        d = '0'+d
        carry = '1'
        n = len(d)
        output = []
        for j in range(n-1,-1,-1):
            output.append('1' if ((carry == '1') ^ (d[j] == '1')) else '0')
            carry = '1' if carry == '1' and d[j] == '1' else '0'
        d = ''.join(output[::-1])
        return d.lstrip('0')
            

if __name__ == '__main__':
    
    a = "11"
    b = "1"
    expected = "100"
    
    # a = "1010"
    # b = "1011"
    # expected = "10101"
    
    # a = "100"
    # b = "110010"
    # expected = '110110'
    
    print(f'a: {a}; b: {b}')
    print(f'expected: {expected}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.addBinary(a,b))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 64 ms, faster than 11.96% of Python3 online submissions for Add Binary.
Memory Usage: 14.3 MB, less than 21.18% of Python3 online submissions for Add Binary.
"""