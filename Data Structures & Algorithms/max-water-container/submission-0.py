class Solution:
    def maxArea(self, heights: List[int]) -> int:
        topArea = float('-inf')
        currArea = topArea
        left = 0
        right = len(heights)-1
        while left < right:
            w = right-left
            h = min(heights[left], heights[right])
            currArea = h * w
            topArea = max(topArea, currArea)

            if heights[left]== h:
                left+=1
            if heights[right] == h:
                right-=1
        return topArea

        