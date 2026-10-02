class Solution:
    def rob(self, nums: List[int]) -> int:
        #rob i and [i+2:n]
        # skip go to next house and make decision again [i+1]
        hashMap = dict()
        def decision(i):
            if i >= len(nums):
                return 0
            if i in hashMap:
                return hashMap[i]
            rob = nums[i] + decision(i+2)
            skip = decision(i+1)
            hashMap[i] = max(rob, skip)
            return hashMap[i]
        return decision(0)