class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid  = (right + left)//2
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile/mid)
            if hours_spent <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left
