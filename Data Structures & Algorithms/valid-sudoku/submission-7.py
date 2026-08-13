class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        box = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]

        for r in range(n):
            for c in range(n):
                box_idx = (r//3)*3 + c//3
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in box[box_idx]) or (board[r][c] in row[r]) or (board[r][c] in col[c]):
                    return False
                
                box[box_idx].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])
        return True  