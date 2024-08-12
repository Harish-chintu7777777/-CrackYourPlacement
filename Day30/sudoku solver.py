

class Solution:
    def isValid(self, row, col, c, board):
        for i in range(9):
            if board[row][i] == c:
                return False
            if board[i][col] == c:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in '123456789':
                        if self.isValid(i, j, c, board):
                            board[i][j] = c
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = '.'  
                    return False 
        return True
