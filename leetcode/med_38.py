"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
which is then converted into a different digit string.

For example, the saying and conversion for digit string "3322251":

two 3's, three 2's, one 5 and one 1 -> "32321511"

E.g.1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

1 -> 11 -> 21 -> 1211 -> 111221 -> 312211

"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = '1'
        j = 1
        while j < n:
            s = self.count_say_seq(s)
            j+=1
        return s
        
    def count_say_seq(self, s: str):
        n = len(s)
        if n == 1:
            return f'1{s}'
        pre = s[0]
        c = 1
        output = ''
        for j in range(1,n):
            if s[j] == pre:
                c+=1
                continue
            else:
                output += f'{c}{pre}'
                pre = s[j]
                c = 1
        output += f'{c}{pre}'
        return output
        

if __name__ == '__main__':
    
    n = 5
    
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    for j in range(10):
        print(sol.countAndSay(j))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 53 ms, faster than 33.27% of Python3 online submissions for Count and Say.
Memory Usage: 14.5 MB, less than 22.89% of Python3 online submissions for Count and Say.
"""