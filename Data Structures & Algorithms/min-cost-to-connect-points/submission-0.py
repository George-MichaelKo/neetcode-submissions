class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, 0)]
        heapq.heapify(heap)
        visited = set()
        minD = 0
        while heap:
          distance,index = heapq.heappop(heap)
          if index in visited:
            continue
          visited.add(index)
          minD += distance
          for i in range(len(points)):
            if i not in visited:
              manhattan = abs(points[index][0]-points[i][0]) + abs(points[index][1]-points[i][1])
              heapq.heappush(heap, (manhattan, i))
        return minD
            
            
          