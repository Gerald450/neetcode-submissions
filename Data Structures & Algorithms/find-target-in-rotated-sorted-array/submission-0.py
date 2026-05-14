class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            
            if target == nums[m]:
                return m
            #[3,4,5,6,1,2]
            #left half (ordered partition)
            if l <= m:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            #right half
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

            
        return -1


