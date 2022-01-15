"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

E.g.1
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

E.g.2:
Input: n = 1
Output: [[1]]
"""
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[]*n]*n
        i = 0
        j = n-1
        num = 1
        layer = 0
        while i <= j:
            if i == j:
                matrix[i].insert(i, num)
                break
            length = j - i # 3
            
            matrix[i] = [ *matrix[i][:layer], *range(num, num+length+1), *matrix[i][-layer:] ]
            matrix[j] = [ *matrix[j][:layer], *range(num+3*length, num + 2*length-1,-1)  , *matrix[j][-layer:] ]
            for p in range(i+1, j):
                matrix[p] = [ *matrix[p][:layer], num+3*length+(j-p), num+length+p-i, *matrix[p][-layer:]]
            num += 4 * length
            i+=1
            j-=1
            layer+=1
        return matrix


if __name__ == '__main__':
    
    n = 3
    
    print(f'n: {n}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.generateMatrix(n))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 28 ms, faster than 90.63% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 14.2 MB, less than 75.92% of Python3 online submissions for Spiral Matrix II.
"""