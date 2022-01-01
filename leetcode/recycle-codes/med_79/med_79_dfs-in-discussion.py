class Solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res

if __name__ == '__main__':
    
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = 'ABCC'
    
    board = [['a']]
    word = 'ab'
    
    board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
    word = "AAAAAAAAAAAAABB"
    
    # board = [["B","B","B","B"],["B","B","B","B"],["B","C","B","B"],["B","B","B","B"],["B","B","B","B"]]
    # word = "BBBBBBBBBBBBBCB"
    
    # board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
    # word = "BBAAAAAAAAAAAAA"
    
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # word = "ABCCED"
    
    # board = [["a"]]
    # word = "b"
    
    for row in board:
        for c in row:
            print(c, end=' ')
        print('')
    print(f'word = {word}')
    print('-'*30)
    sol = Solution()
    from time import time
    start_time = time()
    print(sol.exist(board=board, word=word))
    print(f'duration time: {time() - start_time}')