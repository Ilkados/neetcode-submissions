from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set) 

        for row in range(9):
            for col in range(9):
                digit = board[row][col]

                if digit == ".":
                    continue

                box_key = (row // 3, col // 3)

                if digit in rows[row] : 
                    return False
                
                if digit in columns[col]: 
                    return False

                if digit in squares[box_key]:
                    return False
                
                rows[row].add(digit)
                columns[col].add(digit)
                squares[box_key].add(digit)
        return True
