class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        n = len(board)
        box = defaultdict(set)
        row = defaultdict(set)
        col = defaultdict(set)

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in box[(r//3, c//3)]) or (board[r][c] in row[r]) or (board[r][c] in col[c]):
                    return False
                
                box[(r//3, c//3)].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])
        return True  