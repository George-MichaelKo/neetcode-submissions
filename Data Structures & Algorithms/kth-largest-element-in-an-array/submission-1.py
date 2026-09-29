import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = []
        heapq.heapify(largest)
        for i in range(len(nums)):
            heapq.heappush(largest, nums[i])
            if len(largest) > k:
                heapq.heappop(largest)
        return largest[0]

        