class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0;
        

        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue

            maxl, maxr = height[i], height[i]

            #left
            for l in range(0, i, 1):
                if height[l] > maxl:
                    maxl = height[l]
            for r in range(i, len(height), 1):
                if height[r] > maxr:
                    maxr = height[r]

            res = min(maxr, maxl) - height[i]
            print(res, maxr)
            area += max(0, res)

        return area

