class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #area = length * height
        #area = (l - r) * min(height[l], height[r])
        #use two pointers
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res