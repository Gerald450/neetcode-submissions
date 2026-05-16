class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        input: arr of nums
        output: arr of arr, triplets that sum up to 0

        edge cases: empty, no triplets found

        plan:
        sort
        use two pointers
        make one point stationery, find other two that add to zero
        skip duplicates by incrementing the pointers if prev is same as curr
        add to otp list
        [-2, -2, -1, 0, 1, 1, 2, 4, 5]
        '''

        otp = []
        nums.sort()
        idx = 0

        while idx < len(nums):
            
            #no more solutions
            if nums[idx] > 0:
                break

            #skip duplicates
            while idx < len(nums) and idx > 0 and nums[idx - 1] == nums[idx]:
                idx += 1

            l = idx + 1
            r = len(nums) - 1

            while l < r:
                total = nums[idx] + nums[l] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    otp.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    #skip dups
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                    
            idx += 1

        return otp



        '''
        [-2, -2, -1, 0, 1, 1, 2, 4, 5]
        otp = []
        nums = [-2, -2, -1, 0, 1, 1, 2, 4, 5]
        idx = 0, num = -2
        num > 0, -2 > 0, NO
        l = 1
        r = 8
            1 < 8:
                total = -2 + -2 + 5 = 1
                1 > 0 YES
                r = 7
            1 < 7:
                total = -2 + -2 + 4 = 0
                otp = [[-2, -2, 4]]
                l = 2
            2 < 7:
                ....

        otp = [[-2,-2,4], [-2, 1, 1], [-1, 0, 1]]

        '''



        