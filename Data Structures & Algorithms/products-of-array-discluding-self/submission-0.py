class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prev = [1,1,2,8]
        #post = [48,24,6,1]
        #res =[48,24,12,8]
        prev = [1]* len(nums)
        post = [1]* len(nums)
        res = [1]* len(nums)
        temp = 1
        for i in range(len(nums) - 1):
            prev[i + 1] = temp * nums[i]
            temp = prev[i+1]
        temp = 1

        for i in range(len(nums) - 1)[::-1]:
            post[i] = temp * nums[i + 1]
            temp = post[i]
        
        for i in range(len(nums)):
            res[i] = post[i] * prev[i]
        
        return res
            
            