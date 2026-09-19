class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        seen = set()
        # for each letter recursively check the up right left and down cell letter and to see if they belong to board
        def dfs(i, r, c):
            if i == len(word):
                return True
            if  (r >= row or r < 0) or (c >= col or c < 0):
                return False
            if board[r][c] != word[i]:
                return False
            if (r,c) in seen:
                return False
            seen.add((r,c))
            found = (
            dfs(i+1, r-1, c) or #up
            dfs(i+1, r, c+1) or #right
            dfs(i+1, r+1, c) or #down
            dfs(i+1, r, c-1) #left
            )
            seen.remove((r,c))
            return found


        for r in range(row):
            for c in range(col):
                if dfs(0,r,c):
                    return True
        return False

