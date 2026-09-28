class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for  i in range(9):
            r_seen = set()
            for j in range(9):
                if  board[i][j] in r_seen:
                    return False
                if board[i][j] == ".":
                    continue
                r_seen.add(board[i][j])
        
        for i in range(9):
            c_seen = set()
            for j in range(9):
                if board[j][i] in c_seen:
                    return False
                if board[j][i] == ".":
                    continue
                c_seen.add(board[j][i])
        for start_row in range(0,9,3):
            for start_colum in range(0,9,3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        digit = board[start_row + row][start_colum+col]
                        if digit == ".":
                            continue
                        if digit in seen:
                            return False

                        seen.add(digit)
        return True

