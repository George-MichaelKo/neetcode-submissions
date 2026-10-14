class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # empty chess board n X n
        board = [['.'] * n  for _ in range(n)]
        #have my diagonal and col track
        col = set()
        pDig = set()
        nDig = set()
        output = []
        # start placing 1 queen at a time
        def backtrack(r):
            if r >= n:
                output.append(["".join(row) for row in board])
                return 
            for c in range(n):
            # for each queen i check if the horizontal, vertical and pdiagonals are available then place 
                posD = (r+c)
                negD = (r-c)
            # the i will track the diagonal and vertical of theta queen so another queen don't get placed there
                if posD in pDig or negD in nDig or c in col:
                    continue
                #place
                board[r][c] = 'Q'
                col.add(c)
                pDig.add(posD)
                nDig.add(negD)
            # after placing a q i will check another combination of placement, 
                backtrack(r+1)
            #undo current step 
                board[r][c] = '.'
                col.remove(c)
                pDig.remove(posD)
                nDig.remove(negD)
            # I if i am able to place the last queen then I add that combination to to output
            # return my list of combinations 
        backtrack(0)
        return output
            # time complexity = n.n! 
            # space complexity = nxnXn caus eof teh board i create


        