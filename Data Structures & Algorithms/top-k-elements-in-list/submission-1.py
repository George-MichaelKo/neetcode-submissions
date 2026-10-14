import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = dict()
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        heap = []
        heapq.heapify(heap)
        for key, freq in hashMap.items():
            heapq.heappush(heap, (freq,key))
            if len(heap) > k:
                heapq.heappop(heap)
        order = []
        for x, y in heap:
            order.append(y)
        return order


        