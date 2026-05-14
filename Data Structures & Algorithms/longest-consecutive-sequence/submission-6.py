class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        res = 0
        if len(nums) == 1:
            return 1
        for num in nums:
            if (num - 1) in nums_s:
                continue
            
            else:
                count = 1
                p = num + 1
                while p in nums_s:
                    count += 1
                    p += 1
                res = max(res, count)
        return res