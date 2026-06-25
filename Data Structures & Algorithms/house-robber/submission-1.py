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

        rob1, rob2 = 0, 0

        for n in nums:
            temp = rob2
            rob2 = max(rob2, n + rob1)
            rob1 = temp

        return rob2


        '''
        runtime: O(n)
        space:O(n)
        '''