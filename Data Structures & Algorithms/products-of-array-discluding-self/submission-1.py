class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create array prev for products of all items before current number
        #same as array post

        prev = [1]*len(nums)
        post = [1]*len(nums)
        otp = [1]*len(nums)
        product = 1
        #prev
        #[1,1,2,8]
        for i in range(len(nums) - 1):
            prev[i + 1] = nums[i] * product
            product = prev[i+1]

        product = 1
        #[48,24,6,1]
        for y in range(len(nums)-1)[::-1]:
            post[y] = nums[y+1] * product
            product = post[y]

        for h in range(len(nums)):
            otp[h] = post[h]*prev[h]
        
        return otp
       

    
            
            