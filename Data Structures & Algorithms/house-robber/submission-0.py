class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        input: nums
        output: max money

        edge: just one, empty, negative money

        plan:
        loop through nums
        if len of nums is 1 return the value
        if len is 2 return max
        initialise an output array with first two values nums[0] and max of the two
        loop through and update current index value with max between prev and prev prev + curr
        return last value
        '''

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        

        output = [1] * len(nums)
        output[0] = nums[0]
        output[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            output[i] = max(output[i - 1], output[i - 2] + nums[i])


        return output[-1]


        '''
        runtime: O(n)
        space:O(n)
        '''