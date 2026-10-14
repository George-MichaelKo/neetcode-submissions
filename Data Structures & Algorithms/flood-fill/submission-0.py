from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        sColor = image[sr][sc]
        if sColor == color:
            return image
        image[sr][sc] = color
    
        q = deque([(sr,sc)])
        directions = [(1,0), (0,1),(-1,0),(0,-1)]
        rows = len(image)
        cols = len(image[0])
        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if nr < 0 or nr >= rows or nc<0 or nc>=cols or image[nr][nc] != sColor:
                    continue
                image[nr][nc] = color
                q.append((nr,nc))
        return image

        