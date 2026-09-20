class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #create my output list
        #get my rows and column lenght
        #recursive dfs where explore neighbors that are equal to or less than height

        row = len(heights)
        col = len(heights[0])
        output = []
        pac = set()
        atl = set()
        #dfs
        def dfs(r,c, seen, prevHeight):
            if r >= row or r < 0 or c >= col or c<0 or heights[r][c] < prevHeight:
                return 
            if (r,c) in seen:
                return 
            
            seen.add((r,c))
            dfs(r+1, c,seen, heights[r][c])
            dfs(r,c+1,seen, heights[r][c])
            dfs(r-1, c,seen, heights[r][c])
            dfs(r, c-1,seen, heights[r][c])


        for r in range(row):
            dfs(r,0, pac, heights[r][0]) #left col - pac
            dfs(r,col-1,atl, heights[r][col-1])#right col - atl
        for c in range(col):
            dfs(0,c, pac, heights[0][c]) #top row - pac
            dfs(row-1,c, atl, heights[row-1][c])#bottom row - atl

        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in atl:
                    output.append([r,c])
                
        return output
                

        