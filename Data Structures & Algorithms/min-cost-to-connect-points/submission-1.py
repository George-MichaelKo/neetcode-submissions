class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minArr = [float('inf')] * len(points)
        minArr[0] = 0
        idx = 0 
        minD = 0
        while idx < len(points):
          smallest = float('inf')
          index = -1
          for i in range(len(points)): #find smallest add to minD:
            if i not in visited and minArr[i] < smallest:
                smallest = minArr[i]
                index = i
          visited.add(index)
          minD += minArr[index]
          for i in range(len(points)):
            if i not in visited:  
              manhattan = abs(points[index][0]-points[i][0]) + abs(points[index][1]-points[i][1])
              minArr[i] = min(minArr[i],manhattan)
          idx+=1
        return minD
            
            
          