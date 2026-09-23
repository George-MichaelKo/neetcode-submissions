from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == (rows-1) or c == 0 or c == (cols-1)) and board[r][c] == "O":
                    board[r][c] = "T"
                    q.append((r,c))
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or board[nr][nc]!= "O":
                    continue 
                board[nr][nc] = "T"
                q.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        