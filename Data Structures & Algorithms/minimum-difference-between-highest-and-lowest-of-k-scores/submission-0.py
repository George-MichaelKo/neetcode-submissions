class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        small = float('inf')
        for i in range(n-k+1):
            d = nums[i+k-1] - nums[i]
            small = min(small,d)
        return small

        