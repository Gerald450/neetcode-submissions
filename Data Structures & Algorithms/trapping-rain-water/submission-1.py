class Solution:
    def trap(self, height: List[int]) -> int:
        #area = height[i] * min(maxl, maxR)
        #store maxl, maxR
        #res += area
        res = 0
        l, r = 0, len(height) - 1
        maxl, maxR = height[l], height[r]
        while l < r:
            maxl = max(height[l], maxl)
            maxR = max(height[r], maxR)
            if maxl < maxR:
                
               
                prev = height[l]
                l += 1
                area = max(0, (maxl - height[l])) 
                res += area
                
            
            else:
                preve = height[r]
                r -= 1
                area = max(0, (maxR - height[r]))
                res += area
        return res

    #     class Solution:
    # def trap(self, height: List[int]) -> int:
    #     if not height:
    #         return 0

    #     l, r = 0, len(height) - 1
    #     leftMax, rightMax = height[l], height[r]
    #     res = 0
    #     while l < r:
    #         if leftMax < rightMax:
    #             l += 1
    #             leftMax = max(leftMax, height[l])
    #             res += leftMax - height[l]
    #         else:
    #             r -= 1
    #             rightMax = max(rightMax, height[r])
    #             res += rightMax - height[r]
    #     return res


     
                    

               