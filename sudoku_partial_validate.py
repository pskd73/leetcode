from typing import List

class Solution:
    def isValidGrid(self, board, x, y):
        s, l = set(), 0
        for i in range(x, x+3):
            for j in range(y, y+3):
                if board[i][j] != '.':
                    s.add(board[i][j])
                    l += 1
        return len(s) == l
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sets = [([set(), 0], [set(), 0]) for i in range(9)]
        
        for row in range(9):
            for col in range(9) :
                if board[row][col] != '.':
                    sets[row][0][0].add(board[row][col])
                    sets[row][0][1] += 1

                    sets[col][1][0].add(board[row][col])
                    sets[col][1][1] += 1

                if row % 3 == 0 and col % 3 == 0:
                    if not self.isValidGrid(board, row, col):
                        return False
        
        for st in sets:
            for crst in st:
                if len(crst[0]) != crst[1]:
                    return False
            
        return True


board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

board2 = [
    [".",".","4", ".",".",".", "6","3","."],
    [".",".",".", ".",".",".", ".",".","."],
    ["5",".",".", ".",".",".", ".","9","."],

    [".",".",".", "5","6",".", ".",".","."],
    ["4",".","3", ".",".",".", ".",".","1"],
    [".",".",".", "7",".",".", ".",".","."],

    [".",".",".", "5",".",".", ".",".","."],
    [".",".",".", ".",".",".", ".",".","."],
    [".",".",".", ".",".",".", ".",".","."]
]

s = Solution()
print(s.isValidSudoku(board2))