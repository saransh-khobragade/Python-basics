from typing import List
board = [
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

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic={}
        for i in range(9):
            for j in range(9):
                if board[i][j]=="5":
                    if board[i][j] in dic:
                        print(dic[board[i][j]])
                    else:
                        dic[board[i][j]]={i:i,j:j,'s':1}
        print(dic)


                
    
s = Solution()
s.isValidSudoku(board)