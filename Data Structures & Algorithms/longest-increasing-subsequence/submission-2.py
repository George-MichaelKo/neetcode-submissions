class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            l, r = 0, len(tails)
            while l < r:
                mid = (l+r)//2
                if tails[mid] >= num:
                    r = mid
                else:
                    l = mid + 1
            if l < len(tails):
                tails[l] = num
            else:
                tails.append(num)
        return len(tails)
    