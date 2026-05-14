class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_num = nums[0];
        min_num = nums[0];
        list1 = list()
        max_count = 0
        count = 0

        
        for num in nums:
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num


        for i in range(min_num, max_num + 1):
            list1.append(i)

        max_num = 0

        for i in range(len(list1)-1):
            if list1[i] in nums and list1[i + 1] in nums:
                count = count + 1
            else:
                if count > max_count:
                    max_count = count
                count = 0

        if count > max_count:
            return count + 1
        else:
            return max_count + 1
        
        

        



      
        