from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = dict()
        for i in range(len(tasks)):
            hashMap[tasks[i]] = hashMap.get(tasks[i], 0) + 1
        
        
        ready = [-value for value in hashMap.values()]
        heapq.heapify(ready)
        time = 0
        cool = deque([])
        while ready or cool:
            if cool and time - cool[0][1] >= n + 1:#first bring task that are readdy
                f,last = cool.popleft()
                heapq.heappush(ready,f)

            if ready:
                freq = heapq.heappop(ready)
                count = freq + 1
                if count < 0:#since i am dealing with -negatives
                    cool.append((count, time))
            time+=1
        return time
                
            