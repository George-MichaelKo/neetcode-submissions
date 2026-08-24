class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        inflection = left
        if nums[inflection] <= target <= nums[-1]:
            left = inflection
            right = len(nums) - 1
        else:
            left = 0
            right = inflection - 1
        while left <= right:
            mid = (right + left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1
