class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        minutes = 0 
        fresh = 0 
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        directions = [
        (1,0),#up
        (-1,0),#down
        (0,1),#right
        (0,-1)#left
        ]
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] ==1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1