class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        #["A","B","C","E"],
        #["S","F","C","S"],
        #["A","D","E","E"]

        def dfs(i,j,k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            temp = board[i][j]
            board[i][j] = ''

            if dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1):
                return True
            board[i][j] = temp
            return False

        for i in range(0,len(board)): 
            for j in range(0,len(board[i])):
                if dfs(i,j,0):
                    return True
        return False