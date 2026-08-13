class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        n = len(board)
        box = defaultdict(list)
        row = defaultdict(set)
        col = defaultdict(set)

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in box[(r//3, c//3)]:
                    return False
                elif board[r][c] in row[r]:
                    return False
                elif board[r][c] in col[c]:
                    return False
                box[(r//3, c//3)].append(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])
        return True  