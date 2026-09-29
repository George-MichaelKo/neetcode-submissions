import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for x,y in points:
            distance = math.sqrt(((x)**2 + (y)**2))
            closest.append((distance, x, y))

        output = []
        heapq.heapify(closest)
        for _ in range(k):
            distance, x, y = heapq.heappop(closest)
            output.append([x,y])
        return output
            
        