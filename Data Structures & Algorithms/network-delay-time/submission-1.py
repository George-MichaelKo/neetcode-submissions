from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #build the graph
        network = defaultdict(list)

        for source, target, time in times:
            network[source].append((time,target)) #time, target,
        heap = [(0,k)]
        heapq.heapify(heap) # start, starting time 
        visited = set()
        total = 0
        while heap:
            sTime, node = heapq.heappop(heap)
            
            if node in visited:
                continue
            visited.add(node)
            total = sTime

            for time, neighbor in network[node]:
                heapq.heappush(heap, (sTime + time, neighbor))
            
        if len(visited) == n:
            return total
        return -1  