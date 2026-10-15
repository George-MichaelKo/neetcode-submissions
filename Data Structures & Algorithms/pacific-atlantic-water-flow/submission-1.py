class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        rows = len(heights)
        cols = len(heights[0])

        pBorder = []
        aBorder = []

        output = []

        def bfs(borders, seen):
            q = deque()
            for r,c in borders:
                q.append((r,c))
                seen.add((r,c))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr,nc) in seen or  heights[nr][nc] <  heights[r][c]:
                        continue
                    q.append((nr,nc))
                    seen.add((nr,nc))
        for r in range(rows):
            pBorder.append((r,0))
            aBorder.append((r,cols-1))

        for c in range(cols):
            pBorder.append((0,c))
            aBorder.append((rows-1,c))

        bfs(pBorder, pac)
        bfs(aBorder, atl)

        for r, c in pac:
            if (r,c) in atl:
                output.append([r,c])
        return output
                

        