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
        q = deque([])
        while ready or q:
            if q and time - q[0][1] > n:#first bring task that are readdy
                f,last = q.popleft()
                heapq.heappush(ready,f)

            if ready:
                freq = heapq.heappop(ready)
                count = freq + 1
                if count < 0:#since i am dealing with -negatives
                    q.append((count, time))
            time+=1
        return time
                
            