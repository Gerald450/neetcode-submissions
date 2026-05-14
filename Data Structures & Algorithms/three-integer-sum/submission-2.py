class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        otp = []
        nums.sort() #[-4,-1,-1,0,1,2]
        for index, num in enumerate(nums):
            if num>0:
                break

            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            l = index + 1
            r = len(nums) - 1

            while l < r:
                t_sum = num + nums[l] + nums[r]
                if t_sum > 0:
                    r -= 1
                elif t_sum < 0:
                    l += 1
                elif t_sum == 0:
                    otp.append([num, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
                   
        return otp
