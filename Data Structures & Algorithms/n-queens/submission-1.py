class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #creatwthe board initialiuze with ...
        board = [["."] * n for i in range(n)]
         # i have a set to keep track of unavialble cols, positive diag, anbd negative diag o(1)
        pos_d = set()
        neg_d = set()
        col = set()
        res = []
        row = n 
        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return 
                
            for c in range(n):
                p_dig = row + c
                n_dig = row - c
                if c in col or p_dig in pos_d or n_dig in neg_d:
                    continue
                col.add(c)
                pos_d.add(p_dig)
                neg_d.add(n_dig)
                board[row][c] = "Q"

                backtrack(row+1)

                col.remove(c)
                pos_d.remove(p_dig)
                neg_d.remove(n_dig)
                board[row][c] = "."
        
        backtrack(0)
        return res


        # starting with each q i check the valid position where i can place it
        # checking a cell that the positive and negative diagonal as well as the col is not yet taken 
        # available so another cnfiguartion can be found 


