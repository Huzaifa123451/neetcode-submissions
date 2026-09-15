class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range (9):
            seen = set()
            for i in range (9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in seen:
                    return False
                else:
                    seen.add(board[row][i])
        
        
        for column in range (9):
            seen2 = set()
            for i in range (9):
                if board[i][column] == '.':
                    continue
                if board[i][column] in seen2:
                    return False
                else:
                    seen2.add(board[i][column])
        
        for square in range (9):
            seen3 = set()
            for i in range (3):
                for j in range (3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen3:
                        return False
                    else:
                        seen3.add(board[row][col])
        return True
    

                
