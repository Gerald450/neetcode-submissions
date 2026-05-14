class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0;
        maxl = height[0]
        

        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue

            if height[i] > maxl:
                maxl = height[i]

            maxr =  height[i]

            #left
            # for l in range(0, i, 1):
            #     if height[l] > maxl:
            #         maxl = height[l]
            #right
            for r in range(i, len(height), 1):
                if height[r] > maxr:
                    maxr = height[r]

            res = min(maxr, maxl) - height[i]
            area += max(0, res)

        return area

