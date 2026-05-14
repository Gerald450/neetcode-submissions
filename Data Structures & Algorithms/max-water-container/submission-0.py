class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxW = 0 
        while l < r:
            if heights[l] > heights[r]:
                maxW = max(maxW, heights[r] * abs(l - r))
                r -= 1
            elif heights[l] < heights[r]:
                maxW = max(maxW, heights[l] * abs(l - r))
                l += 1
            else:
                maxW = max(maxW, heights[r] * abs(l - r))
                l += 1
        return maxW
