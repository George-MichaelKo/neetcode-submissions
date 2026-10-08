from collections import defaultdict
class TimeMap:
    def __init__(self):
      self.hashMap = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        best = -1
        l = 0
        r = len(self.hashMap[key])-1
        while l <= r:
          mid = (l+r)//2
          if self.hashMap[key][mid][0] <=  timestamp:
            best = mid
            if self.hashMap[key][mid][0] ==  timestamp:
              break
          if self.hashMap[key][mid][0] < timestamp:
            l = mid + 1
            
          else:
            r = mid - 1
        return self.hashMap[key][best][1]  if best != -1 else ""
          